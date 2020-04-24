import unittest
import huffman
from Huffman_tree import HT


class MyTestCase(unittest.TestCase):

    def test_encodedata(self):
        data = "um ah human huffman is fun i am a fan ha ha ha ha ha ha"
        freqlist = huffman.buildfrequencylist(data)
        B2 = huffman.buildHuffmantree(freqlist)
        res = "001100010011111011100110000111001011100111101110100001110010001010010010110100111100100010110010001001101101011100101110110111011011101101110110111011011101"
        check = huffman.encodedata(B2, data)
        self.assertAlmostEqual(res, check)


if __name__ == '__main__':
    unittest.main()
