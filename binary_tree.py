from typing import Generic, TypeVar, Callable
from stack import Stack
K = TypeVar('K')
I = TypeVar('I')


class BinaryTreeNode(Generic[K, I]):

    def __init__(self, key: K, item: I) -> None:
        self.key = key
        self.item = item
        self.left_child = None
        self.right_child = None

    def __str__(self) -> str:
        return '(' + str(self.key) + ', ' + str(self.item) + ')'


class BinarySearchTree(Generic[K, I]):

    def __init__(self) -> None:
        self.root = None

    def __iter__(self) -> 'BSTInOrderIterator':
        return BSTInOrderIterator(self.root)

    def is_empty(self) -> bool:
        return self.root is None

    def search(self, key: K) -> bool:
        return self.__search_aux(key, self.root)

    def __search_aux(self, key: K, current: BinaryTreeNode[K, I]) -> bool:
        if current is None:
            return False
        elif key < current.key:
            return self.__search_aux(key, current.left_child)
        elif key > current.key:
            return self.__search_aux(key, current.right_child)
        elif key == current.key:
            return True

    def __getitem__(self, key: K) -> I:
        return self.__getitem_aux(key, self.root)

    def __getitem_aux(self, key: K, current: BinaryTreeNode[K, I]) -> I:
        if current is None:
            raise KeyError("Key not found")
        elif key < current.key:
            return self.__getitem_aux(key, current.left_child)
        elif key > current.key:
            return self.__getitem_aux(key, current.right_child)
        elif key == current.key:
            return current.item

    def __setitem__(self, key: K, item: I) -> None:
        self.root = self.__setitem_aux(key, item, self.root)

    def __setitem_aux(self, key: K, item: I, current: BinaryTreeNode[K, I]) -> BinaryTreeNode[K, I]:
        if current is None:
            current = BinaryTreeNode(key, item)
        elif key < current.key:
            current.left_child = self.__setitem_aux(key, item, current.left_child)
        elif key > current.key:
            current.right_child = self.__setitem_aux(key, item, current.right_child)
        else:  # key == current.key => replace item at key
            current.item = item
        return current

    def __delitem__(self, key: K) -> None:
        self.root = self.__delitem_aux(key, self.root)

    def __delitem_aux(self, key: K, current: BinaryTreeNode[K, I]) -> BinaryTreeNode[K, I]:
        if current is None:
            raise KeyError("Key not found")
        elif key < current.key:
            current.left_child = self.__delitem_aux(key, current.left_child)
        elif key > current.key:
            current.right_child = self.__delitem_aux(key, current.right_child)
        else:  # key == current.key, we found node to delete
            if current.left_child is None:
                current = current.right_child
            elif current.right_child is None:
                current = current.left_child
            else:  # has 2 children
                successor = self.__get_successor(current)
                current.key = successor.key
                current.item = successor.item
                current.right_child = self.__delitem_aux(successor.key, current.right_child)
        return current

    # noinspection PyMethodMayBeStatic
    def __get_successor(self, node_to_delete: BinaryTreeNode[K, I]) -> BinaryTreeNode[K, I]:
        current = node_to_delete.right_child
        while current.left_child is not None:
            current = current.left_child
        return current

    def prefix_traversal(self, f: Callable) -> None:
        self.__prefix_traversal_aux(f, self.root)

    def __prefix_traversal_aux(self, f: Callable, current: BinaryTreeNode[K, I]) -> None:
        if current is not None:
            f(current)
            self.__prefix_traversal_aux(f, current.left_child)
            self.__prefix_traversal_aux(f, current.right_child)

    def infix_traversal(self, f: Callable) -> None:
        self.__infix_traversal_aux(f, self.root)

    def __infix_traversal_aux(self, f: Callable, current: BinaryTreeNode[K, I]) -> None:
        if current is not None:
            self.__infix_traversal_aux(f, current.left_child)
            f(current)
            self.__infix_traversal_aux(f, current.right_child)

    def postfix_traversal(self, f: Callable) -> None:
        self.__postfix_traversal_aux(f, self.root)

    def __postfix_traversal_aux(self, f: Callable, current: BinaryTreeNode[K, I]) -> None:
        if current is not None:
            self.__postfix_traversal_aux(f, current.left_child)
            self.__postfix_traversal_aux(f, current.right_child)
            f(current)


class BSTInOrderIterator:
    """Iterates through the binary search tree in order."""

    def __init__(self, root: BinaryTreeNode[K, I]) -> None:
        self.stack = Stack()
        self.stack.push(root)
        self.__push_left_nodes(root)

    def __iter__(self) -> 'BSTInOrderIterator':
        return self

    def __next__(self) -> I:
        if self.stack.is_empty():
            raise StopIteration
        current = self.stack.pop()
        if current.right_child is not None:
            self.stack.push(current.right)
            self.__push_left_nodes(current.right_child)
        return current.item

    def __push_left_nodes(self, current: BinaryTreeNode[K, I]) -> None:
        if current.left_child is not None:
            self.stack.push(current.left_child)
            self.__push_left_nodes(current.left_child)
