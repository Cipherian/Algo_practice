"""
Write a function that takes in a binary search tree and validates whether it is a valid binary search tree.
"""

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


if __name__ == '__main__':
    bs = BST()
    bs.insert(10)
    bs.insert(5)
    bs.insert(10)
    bs.insert(15)
    bs.insert(20)
    bs.insert(30)

    print(validate_bst(bs)) # False

    bs2 = BST()
    bs2.insert(5)
    bs2.insert(10)
    bs2.insert(15)
    bs2.insert(20)
    bs2.insert(30)

    print(validate_bst(bs2)) # True