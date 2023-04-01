"""
Write a function that takes in a list of integers and reconstructs a Binary Tree from it with pre order traversal.
"""

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self, level = 0):
      ret = "\t" * level + str(self.value) + "\n"
      if self.left:
          ret += self.left.__str__(level+1)
      if self.right:
          ret += self.right.__str__(level+1)
      return ret


def reconstructBst(preOrderTraversalValues):
    if not preOrderTraversalValues:
        return None
    
    root_value = preOrderTraversalValues[0]
    left_subtree = []
    right_subtree = []
    
    # Divide the remaining values into left and right subtrees
    for value in preOrderTraversalValues[1:]:
        if value < root_value:
            left_subtree.append(value)
        else:
            right_subtree.append(value)
    
    # Recursively build the left and right subtrees
    left = reconstructBst(left_subtree)
    right = reconstructBst(right_subtree)
    
    return BST(root_value, left, right)


if __name__ == "__main__":
    print(reconstructBst([1, 2, 3, 4, 5, 6, 7, 8, 9]))