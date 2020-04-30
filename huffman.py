__license__ = 'Junior (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: huffman.py 2019-04-01'

"""
Huffman homework
2019
@author: login
"""

from algopy import bintree
from algopy import heap


###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import

###############################################################################
## COMPRESSION

def __frequency(dataIN, c):
    """
    :param dataIN: string
    :param c: character
    :return: frequency of the character c in the string dataIN
    """
    count = 0
    for i in range(len(dataIN)):
        if dataIN[i] == c:
            count += 1
    return count


def __inthelist(L, c):
    """
    :param L: list of Tuple(frequency, char)
    :param c: char
    :return: True if the character c is in the list L or False if not
    """
    for i in range(len(L)):
        if c == L[i][1]:
            return True
    return False


def buildfrequencylist(dataIN):
    """
    Builds a tuple list of the character frequencies in the input.
    """
    L = []
    for i in range(len(dataIN)):
        if not __inthelist(L, dataIN[i]):
            frequency = __frequency(dataIN, dataIN[i])
            L.append((frequency, dataIN[i]))
    return L


def __listtree(inputList):
    """
    :param inputList: list of Tuple(frequency, char)
    :return: a bintree list where each bintree is a leaf and have a Tuple(frequency, char) as key
    """
    for i in range(len(inputList)):
        inputList[i] = bintree.BinTree((inputList[i][0], inputList[i][1]), None, None)
    return inputList


def __2minlist(inputList):
    """
    :param inputList: bintree list (result of __listtree(inputList))
    :return: input list but with a new bintree created from the 2 smallest frequency of the list
    """
    # first min
    mini1 = inputList[0]
    mini1freq = mini1.key[0]
    length = len(inputList)
    index = 0
    for i in range(length):
        if inputList[i].key[0] < mini1freq:
            mini1 = inputList[i]
            mini1freq = mini1.key[0]
            index = i
    (inputList[index], inputList[length - 1]) = (inputList[length - 1], inputList[index])
    mini1 = inputList.pop()
    # second min
    mini2 = inputList[0]
    mini2freq = mini2.key[0]
    index = 0
    length = len(inputList)
    for i in range(length):
        if inputList[i].key[0] < mini2freq:
            mini2 = inputList[i]
            mini2freq = mini2.key[0]
            index = i
    (inputList[index], inputList[length - 1]) = (inputList[length - 1], inputList[index])
    mini2 = inputList.pop()
    inputList.append(bintree.BinTree((mini1freq + mini2freq, None), mini1, mini2))
    return inputList


def __changeKey(B):
    """
    :param B: an huffman tree
    :return: the same huffman tree but the key as changed,
    """
    if B != None:
        if B.key[1] == '_':
            B.key = ' '
        else:
            B.key = B.key[1]
        __changeKey(B.left)
        __changeKey(B.right)
    return B


def buildHuffmantree(inputList):
    """
    Processes the frequency list into a Huffman tree according to the algorithm.
    """
    inputList = __listtree(inputList)
    while len(inputList) > 1:
        inputList = __2minlist(inputList)
    B = __changeKey(inputList[0])
    return B


def __occurences_list(B, L=[], s=""):
    """
    :param B: huffman tree
    :param L: an empty list to fill
    :param s: the occurence string
    :return: a tuple list where a tuple is (B.key, occurence)
    """
    if B != None:
        if B.key != None:
            L.append((B.key, s))
        if B.left != None:
            __occurences_list(B.left, L, s + "0")
        if B.right != None:
            __occurences_list(B.right, L, s + "1")
    return L


def __charinlist(L, c):
    """
    :param L: a list of tuples (char or None, occurence)
    :param c: a char
    :return: True if c is in the list, else False
    """
    length = len(L)
    for i in range(length):
        if L[i][0] == '_' and c == ' ':
            return i, True
        if L[i][0] == c:
            return i, True
    return -1, False


def encodedata(huffmanTree, dataIN):
    """
    Encodes the input string to its binary string representation.
    """
    s = ""
    L = __occurences_list(huffmanTree, [], "")
    length = len(dataIN)
    for i in range(length):
        (index, valid) = __charinlist(L, dataIN[i])
        if valid:
            s += L[index][1]
    return s


def __chartobin(char):
    """
    :param char: a character
    :return: the binary representation of the ascii code of the character
    """
    ascii = ord(char)
    s = ""
    while ascii > 0:
        s += str(ascii % 2)
        ascii = ascii // 2
    while len(s) < 8:
        s += '0'
    res = ""
    index = len(s) - 1
    while index >= 0:
        res += s[index]
        index -= 1
    return res


def __encodetree2(B, s=""):
    """
    :param B: a binarytree
    :param s: s string that represents the tree with 1 and 0
    :return: the binary representation of the tree B
    """
    if B:
        if B.key:
            return '1' + __chartobin(B.key) + __encodetree2(B.left, s) + __encodetree2(B.right, s)
        else:
            return '0' + __encodetree2(B.left, s) + __encodetree2(B.right, s)
    return s


def encodetree(huffmanTree):
    """
    Encodes a huffman tree to its binary representation using a preOrder traversal:
        * each leaf key is encoded into its binary representation on 8 bits preceded by '1'
        * each time we go left we add a '0' to the result
    """
    return __encodetree2(huffmanTree)


def tobinary(dataIN):
    """
    Compresses a string containing binary code to its real binary value.
    """
    index = 0
    res = ""
    full = len(dataIN) // 8
    while index < 8 * full:
        s = ""
        i = 0
        while i < 8:
            s += dataIN[index]
            i += 1
            index += 1
        res += __binarytochar(s)
    reste = len(dataIN) % 8
    i = 0
    s = ""
    while i < reste:
        s += '0'
        i += 1
    align = i
    index = len(dataIN) - reste
    while i < 8:
        s += dataIN[index]
        i += 1
        index += 1
    res += __binarytochar(s)
    return res, align


def compress(dataIn):
    """
    The main function that makes the whole compression process.
    """
    freqList = buildfrequencylist(dataIn)
    huffmanTree = buildHuffmantree(freqList)
    pass


################################################################################
## DECOMPRESSION
def __charintree(B, dataIn, index):
    valid = True
    res = ""
    while valid:
        if B.key != None:
            valid = False
            if B.key == '_':
                res += ' '
            else:
                res = B.key
        elif dataIn[index] == '0':
            B = B.left
        else:
            B = B.right
        index += 1
    return res, index - 1


def decodedata(huffmanTree, dataIN):
    """
    Decode a string using the corresponding huffman tree into something more readable.
    """
    res = ""
    length = len(dataIN)
    index = 0
    resbis, index = __charintree(huffmanTree, dataIN, index)
    res += resbis
    while index < length:
        resbis, index = __charintree(huffmanTree, dataIN, index)
        res += resbis
    return res


def __binarytochar(binarystring):
    """
    :param binarystring: a binary ascii code
    :return: the character of the binary ascii code
    """
    pow = 7
    i = 0
    res = 0
    while i < len(binarystring):
        if binarystring[i] == '1':
            res += 2**pow
        pow -= 1
        i += 1
    return chr(res)


def __reverseList(L):
    """
    :param L: a list
    :return: the list reverse
    """
    Lres = []
    indexL = len(L) - 1
    while indexL >= 0:
        Lres.append(L[indexL])
        indexL -= 1
    L = Lres
    return L


def __charlist(dataIN):
    """
    :param dataIN: the encoded tree
    :return: a tuple (list of char, structure string)
    """
    L = []
    index = 0
    structure = []
    while index < len(dataIN):
        s = ""
        if dataIN[index] == '1':
            structure.append(dataIN[index])
            index += 1
            i = index
            while i < index + 8:
                s += dataIN[i]
                i += 1
            index += 8
            L.append(__binarytochar(s))
        else:
            structure.append(dataIN[index])
            index += 1
    L = __reverseList(L)
    structure = __reverseList(structure)
    return L, structure


def __decodetree(charlist, structure):
    """
    :param dataIN: the encoded data
    :param B: the new tree
    :param index: the index to go through the data
    :return: the tree
    """
    if len(structure) <= 0:
        return None
    index_struct = len(structure) - 1
    if structure[index_struct] == '1':
        structure.pop()
        index = len(charlist) - 1
        key = charlist[index]
        charlist.pop()
        B = bintree.BinTree(key, None, None)
        return B
    elif structure[index_struct] == '0':
        structure.pop()
        B = bintree.BinTree(None, None, None)
        B.left = __decodetree(charlist, structure)
        B.right = __decodetree(charlist, structure)
        return B
    return None


def decodetree(dataIN):
    """
    Decodes a huffman tree from its binary representation:
        * a '0' means we add a new internal node and go to its left node
        * a '1' means the next 8 values are the encoded character of the current leaf         
    """
    (charlist, structure) = __charlist(dataIN)
    return __decodetree(charlist, structure)


def frombinary(dataIN, align):
    """
    Retrieve a string containing binary code from its real binary value (inverse of :func:`toBinary`).
    """
    index = 0
    res = ""
    while index < len(dataIN) - 1:
        char = __chartobin(dataIN[index])
        res += char
        index += 1
    s = __chartobin(dataIN[index])
    i = 0
    while i < len(s):
        if i < align:
            i += 1
            continue
        res += s[i]
        i += 1
    return res


def decompress(data, dataAlign, tree, treeAlign):
    """
    The whole decompression process.
    """
    # FIXME
    pass
