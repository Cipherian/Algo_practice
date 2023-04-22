"""
Implement breadth first search. Visit each item in the queue and return a list of the names.
"""
import unittest
from collections import deque
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
    
    def __str__(self):
        for item in self.children:
            return str(item.name)

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array:list):
        queue = deque([self])
        while queue:
            node = queue.popleft()
            array.append(node.name)
            queue.extend(node.children)
        return array
    

class BreadthFirstSearchTest(unittest.TestCase):
    def test_breadthFirstSearch(self):
        node1 = Node('A')

        node1.addChild('B').addChild('C')
        node1.addChild('D').addChild('E')
        node1.addChild('F').addChild('G')
        node1.addChild('H')

        self.assertEqual(node1.breadthFirstSearch([]), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])

if __name__ == '__main__':
    unittest.main()


