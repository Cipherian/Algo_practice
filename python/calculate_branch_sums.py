"""
Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to
rightmost branch sum.
"""

def branch_sums(root):
    sums = []
    calculate_branch_sums(root, 0, sums)
    return sums

def calculate_branch_sums(node, running_sum, sums):
    if node is None:
        return

    new_running_sum = running_sum + node.value
    if node.left is None and node.right is None:
        sums.append(new_running_sum)

    calculate_branch_sums(node.left, new_running_sum, sums)
    calculate_branch_sums(node.right, new_running_sum, sums)

class BinaryTree:
    def __init__(self, value = 0):
        self.value = value
        self.left = None
        self.right = None

if __name__ == "__main__":
    tree = BinaryTree()
    tree.left = BinaryTree(1)
    tree.right = BinaryTree(2)
    tree.left.left = BinaryTree(3)
    tree.left.right = BinaryTree(4)
    tree.right.left = BinaryTree(5)
    tree.right.right = BinaryTree(6)
    print(branch_sums(tree))
