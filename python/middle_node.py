"""
Write a function that takes in a linked list and returns the middle node of the linked list. 
If there are two middle nodes in the linked list, return the second middle node.
"""
import unittest

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    slow_ptr = linkedList
    fast_ptr = linkedList

    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr


class TestMiddleNode(unittest.TestCase):
    def setUp(self):
        self.linkedList = LinkedList(1)
        self.linkedList.next = LinkedList(2)
        self.linkedList.next.next = LinkedList(3)
        self.linkedList.next.next.next = LinkedList(4)
        self.linkedList.next.next.next.next = LinkedList(5)
        self.linkedList.next.next.next.next.next = LinkedList(6)
        self.linkedList.next.next.next.next.next.next = LinkedList(7)
        self.linkedList.next.next.next.next.next.next.next = LinkedList(8)
        self.linkedList.next.next.next.next.next.next.next.next = LinkedList(9)
        self.linkedList.next.next.next.next.next.next.next.next.next = LinkedList(10)
        self.linkedList.next.next.next.next.next.next.next.next.next.next = LinkedList(11)
        self.linkedList.next.next.next.next.next.next.next.next.next.next.next = LinkedList(12)

        self.middleNode = middleNode(self.linkedList)
    
    def test_middleNode(self):
        self.assertEqual(self.middleNode.value, 7)
        self.assertEqual(self.middleNode.next.value, 8)
        self.assertNotEqual(self.middleNode.next.next.value, 25)
        self.assertAlmostEqual(self.middleNode.next.next.next.value, 10.00000001)
        self.assertGreater(self.middleNode.next.next.next.next.value, 5)
        self.assertLess(self.middleNode.next.next.next.next.next.value, 100)


if __name__ == '__main__':
    unittest.main()