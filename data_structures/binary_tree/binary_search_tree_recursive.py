class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root

    def search(self, root, key):
        if root is None:
            return False
        if key == root.data:
            return True
        elif key < root.data:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.data = self._min_value(root.right)
            root.right = self.delete(root.right, root.data)
        return root

    def _min_value(self, node):
        current = node
        while current.left:
            current = current.left
        return current.data


def binary_search_tree_example():
    bst = BinarySearchTree()
    root = None
    data = [50, 30, 20, 40, 70, 60, 80]
    for value in data:
        root = bst.insert(root, value)
    print("Inorder traversal of BST:")
    bst.inorder(root)
    print("\n\nSearch 40:", bst.search(root, 40))
    print("Search 90:", bst.search(root, 90))
    print("\nDelete 20")
    root = bst.delete(root, 20)
    bst.inorder(root)
    print("\n\nDelete 30")
    root = bst.delete(root, 30)
    bst.inorder(root)
    print("\n\nDelete 50")
    root = bst.delete(root, 50)
    bst.inorder(root)


if __name__ == "__main__":
    binary_search_tree_example()
