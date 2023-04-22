"""
Write a function which uses an Ancestral Tree class and takes in three parameters top_ancestor, descendant_one and descendant_two.
Return the youngest common ancestor to the two descendants.
"""

import unittest

class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None
    
    def __str__(self):
        return self.name

def get_youngest_ancestor(topAncestor, descendantOne, descendantTwo):
    ancestors = {}
    while descendantOne:
        ancestors[descendantOne.name] = descendantOne
        descendantOne = descendantOne.ancestor

    while descendantTwo:
        if descendantTwo.name in ancestors:
            return descendantTwo
        descendantTwo = descendantTwo.ancestor

    return topAncestor


class TestAncestralTree(unittest.TestCase):
    ancestor1 = AncestralTree("root")
    ancestor1.ancestor = AncestralTree("cat")
    ancestor1.ancestor.ancestor = AncestralTree("dog")
    ancestor1.ancestor.ancestor.ancestor = AncestralTree("horse")
    ancestor1.ancestor.ancestor.ancestor.ancestor = AncestralTree("sheep")
    ancestor1.ancestor.ancestor.ancestor.ancestor.ancestor = AncestralTree("cow")
    ancestor1.ancestor.ancestor.ancestor.ancestor.ancestor.ancestor = AncestralTree("elephant")
    ancestor1.ancestor.ancestor.ancestor.ancestor.ancestor.ancestor.ancestor = AncestralTree("zebra")
    ancestor1.ancestor.ancestor.ancestor.ancestor.ancestor.ancestor.ancestor.ancestor = AncestralTree("giraffe")
    ancestor1.ancestor.ancestor.ancestor.ancestor.ancestor.ancestor.ancestor.ancestor.ancestor = AncestralTree("hippo")

    def test_get_youngest_ancestor(self):
        self.assertEqual(get_youngest_ancestor(self.ancestor1, self.ancestor1.ancestor, self.ancestor1.ancestor.ancestor), self.ancestor1.ancestor.ancestor)


  


if __name__ == '__main__':
    unittest.main()