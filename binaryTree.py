class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        # ...


def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)


def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value)


def in_order(node):
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)

in_order(tree)