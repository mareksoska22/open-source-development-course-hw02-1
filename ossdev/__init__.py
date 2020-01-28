# Useful doc on Python magic methods:
# https://rszalski.github.io/magicmethods/
import math


class Vector:
    def __init__(self, arr=None, size=None):
        self.d = arr if arr is not None else (([0] * size) if size else [])

    @classmethod
    def from_arr(cls, arr):
        return Vector(arr=arr)

    @classmethod
    def from_size(cls, size):
        return Vector(size=size)

    def set(self, arr):
        self.d = arr
        return self

    def get(self):
        return self.d

    def __len__(self):
        return len(self.d)

    def __repr__(self):
        return str(self.d)

    def __getitem__(self, item):
        return self.d[item]

    def __hash__(self):
        return sum(self.d)

    def __setitem__(self, key, value):
        self.d[key] = value
        return self

    def __cmp__(self, other):
        if self.length() < other.length():
            return -1
        if self.length() == other.length():
            return 0
        return 1

    def __neg__(self):
        return Vector([-x for x in self.d])

    def __reversed__(self):
        return Vector(list(reversed(self.d)))

    def __add__(self, other):
        if isinstance(other, int):
            return Vector([x + other for x in self.d])
        elif isinstance(other, Vector):
            return Vector([self.d[i] + other[i] for i in range(len(self))])

    # Function for subtraction, not defined for not matching vectors dimensions
    def __sub__(self, other):
        if isinstance(other, int):
            return Vector([x - other for x in self.d])
        elif isinstance(other, Vector):
            return Vector([self.d[i] - other[i] for i in range(len(self))])

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector([x * other for x in self.d])

    def __xor__(self, other):
        if isinstance(other, int):
            return Vector([x ^ other for x in self.d])

    def length(self):
        return math.sqrt(sum(x*x for x in self.d))
