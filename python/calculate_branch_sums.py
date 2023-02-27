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
    def __init__(self, value=0):
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


"""
    1
   / \
  2   3
 / \ / \
4  5 6  7
Starting from the root node 1, the branch sums function is called and passes in the root and hte empty lists sums.
The calculate branch sums function is then called with the arguments node=1, running_sum = 0 and sums = [].
The first step in calculate_branch_sums is to check if the current node is None, which in the first case it is not,
so the funciton continues. Then running_sum is updated to be the sum of the current sum and the value of node.
So in the first case it becomes 0 + 1 = 1. Since the current 1 is not a leaf node, we call calculate_branch_sums twice,
once for the child 2 and once for the child 3. For the left child which is 2 calculate_branch_sums is called with,
node = 2, running_sum = 1, sums = []. The new running_sum is then 1 + 2 = 3. Since 2 is not a leaf node, we call
calculate_branch_sums twice, once for the child 4 and once for the child 5. For the left chiild 4, calculate_branch_sums
is called with node = 4, running_sum = 3, sums = []. The new running_sum is then 3 + 4 = 7. Since 4 is a leaf node,
the running sum is appended to the list, which now becomes sums = [7].  For the right child which is 5, calculate_branch_sums
is called with node=5, running_sum = 3 and sums = [7], the new running sum is 3 + 5 - 8 and since 5 is a leaf node, 8 is
appended to the list, which now becomes sums = [7, 8]. So on and so forth.
"""