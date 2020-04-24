import unittest

def test(x):
    if x > 0:
        return x+1
    else:
        return x+2

def buildList(dataIn):
    return dataIn




class FirstTest (unittest.TestCase):
    def test_Test(self):
        # Check if Test function works
        self.assertAlmostEqual(('bbaabtttaabtctce'),[(4, 'a'), (4, 'b'), (2, 'c'), (1, 'e'), (5, 't')])
        self.assertEqual(buildList('aurelien'),[(2,'e'),(1,'a'),(1,'u'),(1,'r'),(1,'l'),(1,'i'),(1,'n')] )
        self.assertEqual(buildList('aaaapero'),[(4,'a'),(1,'p'),(1,'e'),(1,'r'), (1,'0')])
        self.assertEqual(buildList('wappa'),[(2,'a'),(2,'p'),(1,'w')])
