__license__ = 'Junior (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: huffman.py 2019-04-01'

"""
Huffman homework
2019
@author: titouan.gros
"""

from algopy import bintree
from algopy import heap


###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import

###############################################################################
## COMPRESSION

def buildfrequencylist(dataIN):
    res = []
    i = 0
    length = len(dataIN)
    while i < length:
        if not __IsInTheList(dataIN[i], res):
            res.append((1, dataIN[i]))
        i += 1
    return res


def __IsInTheList(c, list):
    i = 0
    length = len(list)
    while i < length:
        if list[i][1] == c:
            list[i] = (list[i][0] + 1, list[i][1])
            return True
        else:
            i += 1
    return False


###############################################################################


def buildHuffmantree(inputList):
    inputList = __ChangeTree(inputList)
    inputList = __aux(inputList)
    length = len(inputList)
    if (length == 1):
        return NoTuple(inputList[0])


def __aux(list):
    while not len(list) == 1:
        (SmallerFq, SmallerFqbis, list) = __GetSmallerF(list)
        B = bintree.BinTree((SmallerFq.key[0] + SmallerFqbis.key[0], None), SmallerFqbis, SmallerFq)
        list.append(B)
    return list


def __ChangeTree(inputlist):
    res = []
    i = 0
    length = len(inputlist)
    while i < length:
        B = bintree.BinTree(inputlist[i], None, None)
        res.append(B)
        i += 1
    return res


def __GetSmallerF(inputlist):
    i = 0
    length = len(inputlist)
    res = inputlist[0]
    if inputlist[0].key[0] > inputlist[length - 1].key[0]:
        res = inputlist[length - 1]
    else:
        inputlist[i], inputlist[length - 1] = inputlist[length - 1], inputlist[i]
    while i < length:
        if inputlist[i].key[0] < res.key[0]:
            res = inputlist[i]
            inputlist[i], inputlist[length - 1] = inputlist[length - 1], inputlist[i]
        i += 1
    inputlist.pop()
    length -= 1
    i = 0
    newres = inputlist[0]
    if newres.key[0] > inputlist[length - 1].key[0]:
        newres = inputlist[length - 1]
    else:
        inputlist[i], inputlist[length - 1] = inputlist[length - 1], inputlist[i]
    while i < length:
        if inputlist[i].key[0] < newres.key[0]:
            newres = inputlist[i]
            inputlist[i], inputlist[length - 1] = inputlist[length - 1], inputlist[i]
        i += 1
    inputlist.pop()
    return (res, newres, inputlist)

def NoTuple(B):
    if B:
        if B.key[1] == None:
            B.key = None
        else:
            B.key = B.key[1]
        NoTuple(B.left)
        NoTuple(B.right)
    return B

###############################################################################


def encodedata(huffmanTree, dataIN):
    i = 0
    length = len(dataIN)
    res = ""
    while i < length:
        res += __searchOcc(huffmanTree, dataIN[i])
        i+=1
    return res


def __searchOcc(B, c, occ=""):
    """
    B non empty tree
    occ: the occurence of the root
    """
    if B.left == None:
        if B.key == c:
            return occ
        else:
            return None
    else:
        res = __searchOcc(B.left, c, occ + '0')
        if res != None:
            return res
        else:
            return __searchOcc(B.right, c, occ + '1')


# occ is built going up
def __searchOcc2(B, c):
    """
    B non empty tree
    """
    if B.left == None:
        if B.key == c:
            return ""
        else:
            return None
    else:
        res = __searchOcc2(B.left, c)
        if res != None:
            return '0' + res
        else:
            res = __searchOcc(B.right, c)
            if res != None:
                return '1' + res
            else:
                return None


def __searchOcc(B, c):
    if B == None:
        return None
    else:
        return __searchOcc2(B, c)

###############################################################################

def encodetree(huffmanTree):
    """
    Encodes a huffman tree to its binary representation using a preOrder traversal:
        * each leaf key is encoded into its binary representation on 8 bits preceded by '1'
        * each time we go left we add a '0' to the result
    """
    # FIXME
    pass


def tobinary(dataIN):
    """
    Compresses a string containing binary code to its real binary value.
    """
    # FIXME
    pass


def compress(dataIn):
    """
    The main function that makes the whole compression process.
    """

    # FIXME
    pass


################################################################################
## DECOMPRESSION

def decodedata(huffmanTree, dataIN):
    char = ""
    i = 0
    length = len(dataIN)
    char, i = __decodechar(huffmanTree,dataIN, 0)
    while i < length:
        charbis, i = __decodechar(huffmanTree,dataIN, i)
        char += charbis

    return char

def __decodechar(B, stri, i):
    bol = True
    res = ""
    while bol:
        if B.key != None :
            bol = False
            res = str(B.key)
        elif stri[i] == '0':
            B = B.left
        elif stri[i] == '1':
            B = B.right
        i += 1

    return res, i-1

def printTree(B, s=""):
    '''
    simple ASCII display tree directory like...
    '''
    if B != None:
        if B.key == None:
            key = str(B.key)
        else:
            key = B.key
        print(s, '- ', key)
        printTree(B.left, s + "  |")
        printTree(B.right, s + "   ")

"""L = buildfrequencylist("um ah human huffman is fun i am a fan ha ha ha ha ha ha")
B = buildHuffmantree(L)
printTree(B)

s = encodedata(B,"um ah human huffman is fun i am a fan ha ha ha ha ha ha")
print(s)
sbis = decodedata(B,s)
print(sbis)"""


def decodetree(dataIN):
    """
    Decodes a huffman tree from its binary representation:
        * a '0' means we add a new internal node and go to its left node
        * a '1' means the next 8 values are the encoded character of the current leaf         
    """
    # FIXME
    pass


def frombinary(dataIN, align):
    """
    Retrieve a string containing binary code from its real binary value (inverse of :func:`toBinary`).
    """
    # FIXME
    pass


def decompress(data, dataAlign, tree, treeAlign):
    """
    The whole decompression process.
    """
    # FIXME
    pass
