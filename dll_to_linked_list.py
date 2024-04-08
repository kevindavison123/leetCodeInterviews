class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinaryTree:
    root, head = None, None

    def BTtoDLL(self, root: Node):
        if root is None:
            return
        self.BTtoDLL(root.right)
        root.right = self.head

        if self.head is not None:
            self.head.left = root

        self.head = root

        self.BTtoDLL(root.left)

    @staticmethod
    def print_list(head: Node):
        print('Extracted Double Linked List: ')
        while head is not None:
            print(head.data, end = ' ')
            head = head.right

if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.right = Node(6)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(4)
    tree.root.right.right = Node(8)
    tree.root.left.left.left = Node(0)
    tree.root.left.left.right = Node(2)
    tree.root.right.right.left = Node(7)
    tree.root.right.right.right = Node(9)

    tree.BTtoDLL(tree.root)
    tree.print_list(tree.head)
