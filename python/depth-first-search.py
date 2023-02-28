"""
You're given a Node class which has name and an array of optional child nodes.Implement a depthfirst search, store all
nodes name in an array and return it
"""


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def depth_first_search(root_node):
    if root_node is None:
        return []
    else:
        result = []
        for child in root_node.children:
            result += depth_first_search(child)
        result.append(root_node.name)
        return result


if __name__ == "__main__":
    root = Node("root")
    root.add_child(Node("child1"))
    root.add_child(Node("child2"))
    root.add_child(Node("child3"))
    print(depth_first_search(root))
