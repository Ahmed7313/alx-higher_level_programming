#!/usr/bin/python3
"""Module for Node and SinglyLinkedList classes."""

class Node:
    """Class to define a node for a singly linked list."""
    def __init__(self, data, next_node=None):
        """Initialize a Node with data and a pointer to the next node.

        Args:
            data (int): The data stored in the node.
            next_node (Node, optional): The next node in the list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: Gets the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node, ensuring it is an integer.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Node or None: Gets the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the list.

        Raises:
            TypeError: If the value is neither None nor a Node instance.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Class to define a singly linked list."""
    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Return the string representation of the list, one node value per line."""
        values = []
        current = self.__head
        while current:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Inserts a new Node into the list at the correct sorted position.

        Args:
            value (int): The data value to insert into the list.
        """
        new_node = Node(value)
        if not self.__head or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

# Example usage
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)

