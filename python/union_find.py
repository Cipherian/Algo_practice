"""
Write a union find data structure that can be used to efficiently find the union of two sets of integers.
"""

import unittest

class UnionFind:
    def __init__(self):
        self.parent = {}

    def createSet(self, value):
        self.parent[value] = value

    def find(self, value):
        if value not in self.parent:
            return None
        while value != self.parent[value]:
            value = self.parent[value]
        return value

    def union(self, valueOne, valueTwo):
        rootOne = self.find(valueOne)
        rootTwo = self.find(valueTwo)
        if rootOne is None or rootTwo is None:
            return
        if rootOne != rootTwo:
            self.parent[rootTwo] = rootOne

class TestUnionFind(unittest.TestCase):
    def setUp(self):
        self.union = UnionFind()
        self.union.createSet(1)
        self.union.createSet(2)
        self.union.createSet(3)
        self.union.createSet(4)
        self.union.createSet(5)
        self.union.createSet(6)
        self.union.createSet(7)
        self.union.createSet(8)
        self.union.createSet("hello")
    
    def test_find(self):
        self.assertEqual(self.union.find(1), 1)
        self.assertEqual(self.union.find(2), 2)
        self.assertEqual(self.union.find(3), 3)
        self.assertEqual(self.union.find(4), 4)
        self.assertEqual(self.union.find(5), 5)
        self.assertEqual(self.union.find(6), 6)
        self.assertEqual(self.union.find(7), 7)
        self.assertEqual(self.union.find(8), 8)
        self.assertEqual(self.union.find("hello"), "hello")

if __name__ == "__main__":
    unittest.main()
