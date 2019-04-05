"""
An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields,
it holds a field named both, which is an XOR of the next node and the previous node.
Implement an XOR linked list; it has an add(element) which adds the element to the end,
and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python),
you can assume you have access to
get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""

import ctypes


class XorList(object):

    class Node(object):
        def __init__(self, val):
            self.val = val
            self.both = 0

    def __init__(self):
        self.count = 0
        self.begin = XorList.Node(None)
        self.end = XorList.Node(None)
        self.begin.both ^= get_pointer(self.end)
        self.end.both ^= get_pointer(self.begin)
        self._nodes = []  # Have to do this to avoid garbage collection

    def add(self, element):
        prev = dereference_pointer(self.end.both)
        prev.both ^= get_pointer(self.end)
        self.end.both = 0
        n = XorList.Node(element)
        self._nodes.append(n)
        prev.both ^= get_pointer(n)
        n.both ^= get_pointer(prev)
        n.both ^= get_pointer(self.end)
        self.end.both ^= get_pointer(n)
        self.count += 1

    def get(self, index):
        if index > self.count:
            raise IndexError(f'Index out of bounds')
        prev_ptr = 0
        node = self.begin
        for _ in range(index + 1):
            next_ptr = node.both ^ prev_ptr
            prev_ptr = get_pointer(node)
            node = dereference_pointer(next_ptr)
        return node.val


def get_pointer(obj):
    """return &obj"""
    return id(obj)


def dereference_pointer(ptr):
    """return *ptr
    If the object at ptr no longer exists behaviour is undefined, avoid garbage collection"""
    return ctypes.cast(ptr, ctypes.py_object).value


def main():
    l = XorList()
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)
    assert l.get(0) == 1
    assert l.get(3) == 4


if __name__ == '__main__':
    main()
