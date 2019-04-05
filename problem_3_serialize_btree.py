"""
Given the root to a binary tree, implement serialize(root),
which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

import io


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):

    # Init
    nodes = [node]
    next_nodes = []
    builder = io.StringIO()

    # Serialize
    while nodes:
        for n in nodes:
            builder.write(n.val)
            builder.write('\n')
            if n.left:
                next_nodes.append(n.left)
            if n.right:
                next_nodes.append(n.right)
        nodes, next_nodes = next_nodes, []

    return builder.getvalue()


def deserialize(data):

    # Init
    reader = io.StringIO(data)
    root = Node(reader.readline()[:-1])
    nodes = [root]
    next_nodes = []

    line = reader.readline()[:-1]
    while line:
        for n in nodes:
            left = line
            right = reader.readline()[:-1]
            if not left:
                break
            left = Node(left)
            n.left = left
            next_nodes.append(left)
            if right:
                right = Node(right)
                n.right = right
                next_nodes.append(right)
            line = reader.readline()[:-1]
        nodes, next_nodes = next_nodes, []

    return root


def main():
    node = Node('root',
                Node('left',
                     Node('left.left'), Node('left.right')),
                Node('right',
                     Node('right.left'), Node('right.right')))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    assert deserialize(serialize(node)).right.left.val == 'right.left'


if __name__ == '__main__':
    main()
