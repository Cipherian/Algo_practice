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