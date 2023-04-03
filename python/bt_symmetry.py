"""
Write a function that takes in a binary tree and determines whether it is symmetric or not.
"""

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    def is_symmetric(node1, node2):
        # base case: if both nodes are empty, they are symmetric
        if node1 is None and node2 is None:
            return True
        # if one node is empty and the other is not, they are not symmetric
        elif node1 is None or node2 is None:
            return False
        # if the values of the nodes are different, they are not symmetric
        elif node1.value != node2.value:
            return False
        # recursively check the left and right subtrees
        else:
            return is_symmetric(node1.left, node2.right) and is_symmetric(node1.right, node2.left)

    # check if the tree is symmetric by comparing its left and right subtrees
    if tree is None:
        return True
    else:
        return is_symmetric(tree.left, tree.right)


if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.left = BinaryTree(2)
    tree.right = BinaryTree(3)
    tree.left.left = BinaryTree(4)
    tree.left.right = BinaryTree(5)
    tree.right.left = BinaryTree(6)
    tree.right.right = BinaryTree(7)
    print(symmetricalTree(tree)) # false
    tree2 = BinaryTree(1)
    tree2.left = BinaryTree(2)
    tree2.right = BinaryTree(2)
    tree2.left.left = BinaryTree(3)
    tree2.left.right = BinaryTree(3)
    tree2.right.left = BinaryTree(3)
    tree2.right.right = BinaryTree(3)
    print(symmetricalTree(tree2)) # true
