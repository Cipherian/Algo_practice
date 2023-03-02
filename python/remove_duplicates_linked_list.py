"""
Write a function which takes in a linked list and removes any duplicates from it.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node


def remove_duplicates(linked_list: LinkedList) -> LinkedList:
    duplicates = {}
    previous_node = None
    current_node = linked_list.head
    while current_node:
        if current_node.value in duplicates:
            previous_node.next = current_node.next
        else:
            duplicates[current_node.value] = True
            previous_node = current_node
        current_node = current_node.next
    return linked_list


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.insert(5)
    linked_list.insert(5)
    linked_list.insert(5)
    linked_list.insert(5)
    linked_list.insert(9)
    linked_list.insert(10)
    linked_list.insert(11)
    linked_list.insert(11)
    linked_list.insert(11)
    linked_list.insert(11)
    linked_list.insert(15)
    linked_list.insert(16)
    linked_list.insert(17)
    linked_list.insert(18)
    linked_list.insert(19)
    linked_list.insert(20)
    test_list = []
    remove_duplicates(linked_list)
    while linked_list.head:
        test_list.append(linked_list.head.value)
        linked_list.head = linked_list.head.next
    print(test_list)
