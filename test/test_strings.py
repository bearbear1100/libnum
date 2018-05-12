#-*- coding:utf-8 -*-

import unittest
from libnum import *
import os

class StringsTest(unittest.TestCase):
    
    def test_ns(self):
        s = b"long string to test"
        val = 2418187513319072758194084480823884981773628276
        self.assertEqual(s2n(s), val)
        self.assertEqual(n2s(val), s)
        self.assertRaises(TypeError, s2n, 100)
        self.assertRaises(TypeError, n2s, "qwe")

    def test_bs(self):
        a = os.urandom(100)
        b = "".join(map(chr, a))
        print(s2b(a) == s2b(b))
        a == s2b(b2s(a))
        self.assertEqual( a, switchBS(switchBS(a)))
        self.assertEqual( s2b(a) == s2b(b) )
        self.assertEqual( b2s('10'), '\x02')
        self.assertEqual( b2s(b'10'), '\x02')


if __name__ == "__main__":
    unittest.main()
