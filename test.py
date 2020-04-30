import huffman
import Huffman_tree
import huffman2


def printTree(B, s=""):
    '''
    simple ASCII display tree directory like...
    '''
    if B != None:
        if B.key == ' ':
            B.key = '_'
        print(s, '- ', B.key)
        printTree(B.left, s + "  |")
        printTree(B.right, s + "   ")


data = "um ah human huffman is fun i am a fan ha ha ha ha ha ha"
l = huffman.buildfrequencylist(data)
#print(l)
B = huffman.buildHuffmantree(l)
#printTree(B, "")
encodedata = huffman.encodedata(B, data)
#print(encodedata)
decodedata = huffman.decodedata(B, encodedata)
#print(decodedata)
encodetree = huffman.encodetree(B)
#print(encodetree)
encodetree2 = huffman.encodetree(Huffman_tree.HT)
charlist = huffman.__charlist(encodetree)
#print(charlist)
decodetree = huffman.decodetree(encodetree)
#printTree(decodetree)
#printTree(B)
#print(decodetree == B)
tobinary, align = huffman.tobinary(encodedata)
#print(align)
#print(tobinary)
frombinary = huffman.frombinary(tobinary, align)
#print(frombinary)

