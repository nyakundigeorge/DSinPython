from Exceptions import Empty


class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage"""

    # ----------------------------nested _Node Class ----------------------#
    class _Node:
        """Lightweight, non public class for storing a singly linked list"""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize node's fielse
            self._element = element  # reference to user's elements
            self._next = next  # reference to next node

    # --------------------------- stack methods -------------------------------
    def __init__(self):
        """Create and empty stack"""
        self._head = None  # reference to the head node
        self._size = 0  # number of stack elements

    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack"""
        self._head = self._Node(e, self._head)  # create and link a new node
        self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack


            Raise Empty exception if the stack is empty
        """

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element  # top of the stack is at head of list

    def pop(self):
        """Remove and return the selement from the top of the stack (i.e LIFO)

        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
