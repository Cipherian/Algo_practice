"""
Write a function that takes in a binary tree and inverts it.
"""
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return f"({str(self.left)} <- {str(self.value)} -> {str(self.right)})"


def invertBinaryTree(tree):
    if tree is None:
        return
    
    # Swap the left and right subtrees
    tree.left, tree.right = tree.right, tree.left
    
    # Recursively invert the left and right subtrees
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)



if __name__ == "__main__":
    BT = BinaryTree(1)
    BT.left = BinaryTree(2)
    BT.right = BinaryTree(3)
    BT.left.left = BinaryTree(4)
    BT.left.right = BinaryTree(5)
    BT.right.left = BinaryTree(6)
    BT.right.right = BinaryTree(7)
    print(BT)
    invertBinaryTree(BT)
    print(BT)






