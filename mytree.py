class MyTree(object):
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.value = value


def insert(root, node):
    if root is None:
        return MyTree(node)
    else:
        if root.value > node:
            root.left_child = insert(root.left_child, node)
            if root.left_child is None:
                root.left_child = node
        elif root.value < node:
            root.right_child = insert(root.right_child, node)
            if root.right_child is None:
                root.right_child = node
        else:
            pass
    return root


def create_tree(array):
    root = None
    for word in array:
        root = insert(root, word)
    return root


def in_order_print(root):
    if not root:
        return
    in_order_print(root.left_child)
    print(root.value)
    in_order_print(root.right_child)


def pre_order_print(root):
    if not root:
        return
    print(root.value)
    pre_order_print(root.left_child)
    pre_order_print(root.right_child)
