"""
Write a function that takes in a Binary Tree with at least one node and checks if that Binary Tree can be split into two Binary Trees of equal sum
by removing a single edge. If the split is possible return the new sum of each binary tree, otherwise return 0.
"""
import unittest

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def split_binary_tree(tree, total = 0):
    total = set()
    tree_sum = helper(tree, total)
    half_tree_sum = tree_sum / 2
    return half_tree_sum if half_tree_sum in total else 0


def helper(tree, total: set) -> int:
    if tree is None:
        return 0
    
    sum_left = helper(tree.left, total)
    sum_right = helper(tree.right, total)
    curr_sum = tree.value + sum_left + sum_right
    total.add(curr_sum)

    return curr_sum



class TestBinaryTree(unittest.TestCase):
    def test_split_binary_tree(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(2)
        tree.right = BinaryTree(-3)
        tree.left.left = BinaryTree(4)
        tree.left.right = BinaryTree(-2)
        tree.right.left = BinaryTree(-6)
        tree.right.right = BinaryTree(7)
        tree.left.left.left = BinaryTree(-8)
        tree.left.left.right = BinaryTree(-9)
        tree.left.right.left = BinaryTree(10)
        self.assertEqual(split_binary_tree(tree), -2)

    
    def test_split_binary_tree2(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(2)
        tree.right = BinaryTree(-3)
        tree.left.left = BinaryTree(4)
        tree.left.right = BinaryTree(4)
        tree.right.left = BinaryTree(-6)
        self.assertEqual(split_binary_tree(tree), 0)
                         
if __name__ == '__main__':
    unittest.main()