
"""
 Write a function that takes in a binary search tree and a
target integer value, and returns the closest value to that target value
contained in the binary search tree.
"""


def find_closest_value(tree, target:int)-> int:
    """
    :param tree:
    :param target: int
    :return: int
    """
    closest = float('inf')
    """
    closest is initialized to positive infinity, ensure that the first value 
    that the loop encounters will always be closer
    than infinity and will become the closest value.
    """

    while tree:
        if abs(tree.value - target) < abs(closest - target):
            closest = tree.value

        if tree.value < target:
            tree = tree.right
        elif tree.value > target:
            tree = tree.left
        else:
            return tree.value

    return closest

"""

The first node is initialized to 4. if the absolute difference between the current node value and hte target, 
is less than the absolute difference between the closest value and the target. Then the current node's value becomes 
the closest value.If the current node's value is less than the target, then it visits the right child, otherwise if it 
is greater, then it visits the left child. Since 3 is less than 4, we go to the left side of the tree and then tree
becomes 2, and since the target is 3 and 3 is greater than 2 it visits the right child. And then it finds 3 and then
returns that value.

Target is 3
        4
       / \
      2   5
     / \
    1   3
"""


