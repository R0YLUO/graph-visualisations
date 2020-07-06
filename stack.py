"""Implementation of a stack using a python list"""

from typing import Generic, TypeVar
T = TypeVar('T')


class Stack(Generic[T]):

    def __init__(self) -> None:
        """Instantiates an empty list"""
        self.length = 0
        self.list = []

    def __len__(self) -> int:
        """Length of our stack"""
        return self.length

    def is_empty(self) -> bool:
        return len(self) == 0

    def push(self, item: T) -> None:
        """Add item to top of stack"""
        self.list.append(item)
        self.length += 1

    def pop(self) -> T:
        """Remove item from top of stack and return it"""
        if not self.is_empty():
            self.length -= 1
            return self.list.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self) -> T:
        """Look at item at top without removing"""
        if not self.is_empty():
            return self.list[len(self) - 1]
        else:
            raise Exception("Stack is empty")

    def __str__(self) -> str:
        """Prints contents in stack from top to bottom."""
        n = len(self)
        output = ""
        if n == 0:
            return output
        else:
            output += '['
            output += str(self.list[n-1])
            for i in range(n - 2, -1, -1):
                output += ", " + str(self.list[i])
            output += ']'
            return output
