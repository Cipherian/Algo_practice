"""
Write a function that takes in a binary search tree and validates whether it is a valid binary search tree.
"""
import unittest

class BST:
    def __init__(self, value=float("inf"), left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def insert(self, value):
      if value < self.value:
          if self.left is None:
              self.left = BST(value)
          else:
              self.left.insert(value)
      else:
          if self.right is None:
              self.right = BST(value)
          else:
              self.right.insert(value)
      return self


def validate_bst(root, left_parent=float('-inf'), right_parent=float('inf')):
    if root is None:
        return True

    if root.value <= left_parent:
        return False
    if root.value > right_parent:
        return False

    left = validate_bst(root.left, left_parent, root.value)
    right = validate_bst(root.right, root.value, right_parent)

    if left and right:
        return True

    return False

class TestValidateBST(unittest.TestCase):
    def test_validate_bst(self):
        bst = BST()
        bst.insert(10)
        bst.insert(5)
        bst.insert(10)
        bst.insert(15)
        bst.insert(20)
        bst.insert(30)
    
        self.assertFalse(validate_bst(bst))
    
    def test_validate_bst_2(self):
        bst = BST()
        bst.insert(5)
        bst.insert(10)
        bst.insert(15)
        bst.insert(20)
        bst.insert(30)

        self.assertTrue(validate_bst(bst))

if __name__ == '__main__':
    unittest.main()
    