"""
write a function that takes in an array of integers and converts it into a balanced binary search tree.
"""

class BST:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self, level = 0):
      ret = "\t" * level + str(self.value) + "\n"
      if self.left:
          ret += self.left.__str__(level+1)
      if self.right:
          ret += self.right.__str__(level+1)
      return ret

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def convert_to_bst(arr):
    if not arr:
        return None
    
    mid = len(arr) // 2
    root = BST(arr[mid])
    root.left = convert_to_bst(arr[:mid])
    root.right = convert_to_bst(arr[mid + 1:])

    return root


if __name__ == "__main__":
    bst = BST()
    test_list = [1, 2, 3, 4, 5, 6, 7]
    print(convert_to_bst(test_list))