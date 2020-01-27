#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ossdev

import unittest
from ossdev import Vector


class VectorTest(unittest.TestCase):
    """Simple vector tests"""

    def __init__(self, *args, **kwargs):
        super(VectorTest, self).__init__(*args, **kwargs)

    def test_add(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        c = a + b

        self.assertEqual(c.get(), [3, 3, 3, 3])

    def test_dot(self):
        a = Vector([1, 2])
        b = Vector([2, -1])
        self.assertEqual(a.dot(b), 0)

    def test_lenght(self):
        self.assertAlmostEqual(Vector([2, 4]).length(), 4.47213595499, 3)
        self.assertAlmostEqual(Vector([2, 4, 5]).length(), 6.708203932499369, 3)
        return


    def test_length(self):
        a = Vector([4, 4, 1])
        b = Vector([1, 4, 4, 0, 0])
        c = Vector([2, 2, 2, 2])

        self.assertEqual(a.length(), b.length())
        self.assertEqual(c.length(), 4)


    def test_cmp(self):
        a = Vector([1, 2, 1, 3])
        b = Vector([1, 2, 1, 3])
        c = Vector([3, 2, 1, 0])
        d = Vector([3, 2, 1])
        e = Vector([1, 3, 2])

        self.assertEqual(a.__cmp__(b), 0)
        self.assertEqual(a.__cmp__(c), 1)
        self.assertEqual(c.__cmp__(b), -1)
        self.assertEqual(c.__cmp__(d), 0)
        self.assertEqual(c.__cmp__(e), 0)

    def test_neg(self):
        a = Vector([1, 2, 0, 2])
        b = Vector([-1, -2, 0, -2])

        self.assertEqual(a.__neg__().get(), b.get())
        self.assertNotEqual(a.__neg__().get(), a.get())

    def test_reversed(self):
        a = Vector([1, 10, 15, 4])
        b = Vector([4, 15, 10, 1])
        c = Vector

        self.assertEqual(a.__reversed__().get(), b.get())
        self.assertNotEqual(a.__reversed__().get(), a.get())

    def test_sub(self):
        a = Vector([1, 0, 0, 2])
        b = Vector([2, 3, 3, 3])

        self.assertEqual(b.__sub__(a).get(), [1, 3, 3, 1])
        self.assertEqual(b.__sub__(3).get(), [-1, 0, 0, 0])

    def test_mul(self):
        a = Vector([2, 3, 3, 0])
        b = Vector([20, 30, 30, 0])

        self.assertEqual(a.__mul__(1).get(), a.get())
        self.assertEqual(a.__mul__(10).get(), b.get())
        self.assertEqual(a.__mul__(-1).get(), a.__neg__().get())

    def test_xor(self):
        a = Vector([2, 2, 2, 2])
        b = Vector([3, 2, 2, 3])

        self.assertEqual(a.__xor__(2).get(), [0, 0, 0, 0])
        self.assertEqual(b.__xor__(3).get(), [0, 1, 1, 0])

    def test_and(self):
        a = Vector([3, 2, 2, 3])
        b = Vector([1, 1, 1, 1])

        self.assertEqual(a.__and__(a).get(), a.get())
        self.assertEqual(b.__and__(a).get(), [1, 0, 0, 1])
        self.assertEqual(a.__and__(b).get(), [1, 0, 0, 1])
        self.assertEqual(a.__and__(0).get(), [0, 0, 0, 0])

    def test_setitem(self):
        a = Vector([1, 2, 3, 4, 5])

        a.__setitem__(2, 10)
        a.__setitem__(0, 0)
        self.assertEqual(a.get(), [0, 2, 10, 4, 5])

if __name__ == "__main__":
    unittest.main()  # pragma: no cover
