"""
Given a binary search tree (BST) with duplicates, find the kth largest element in the BST. If the k is 3, return the 3rd largest element.
"""


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    stack = []
    count = 0
    current = tree
    
    while current or stack:
        if current:
            stack.append(current)
            current = current.right
        else:
            node = stack.pop()
            count += 1
            if count == k:
                return node.value
            current = node.left


if __name__ == '__main__':
    bst = BST(10)
    bst.left = BST(5)
    bst.left.left = BST(3)
    bst.left.right = BST(7)
    bst.right = BST(15)
    bst.right.left = BST(13)
    bst.right.right = BST(17)

    print(findKthLargestValueInBst(bst, 3)) # 13

"""
We start by initializing an empty stack, a count variable set to 0, and a current variable set to the root node.
We loop while the current node is not None or the stack is not empty.
If the current node is not None, we push it onto the stack and set the current node to its right child. This allows us to traverse the tree in reverse order (right subtree, current node, left subtree).
If the current node is None, we pop the last node from the stack, increment the count variable, and check if the count is equal to k. If it is, we return the value of the current node. 
If it's not, we set the current node to the left child of the node we just popped, and continue the traversal.

"""