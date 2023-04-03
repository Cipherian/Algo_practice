"""
Write a function that merges two binary trees, if two nodes overlap then sum the values. 
"""

class BinaryTree:
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


def mergeBinaryTrees(tree1, tree2):
    # base cases: if either tree is empty, return the other tree
    if tree1 is None:
        return tree2
    elif tree2 is None:
        return tree1
    
    # create a new node with the sum of the values of the two input nodes
    newNode = BinaryTree(tree1.value + tree2.value)
    
    # recursively merge the left and right subtrees
    newNode.left = mergeBinaryTrees(tree1.left, tree2.left)
    newNode.right = mergeBinaryTrees(tree1.right, tree2.right)
    
    return newNode

if __name__ == "__main__":
    bt = BinaryTree(1)
    bt.left = BinaryTree(2)
    bt.right = BinaryTree(3)
    bt.left.left = BinaryTree(4)
    bt.left.right = BinaryTree(5)
    bt.right.left = BinaryTree(6)
    bt.right.right = BinaryTree(7)
    bt2 = BinaryTree(8)
    bt2.left = BinaryTree(9)
    bt2.right = BinaryTree(10)
    bt2.left.left = BinaryTree(11)
    bt2.left.right = BinaryTree(12)
    bt2.right.left = BinaryTree(13)
    bt2.right.right = BinaryTree(14)
    bt2.right.right.left = BinaryTree(15)
    print(mergeBinaryTrees(bt, bt2))