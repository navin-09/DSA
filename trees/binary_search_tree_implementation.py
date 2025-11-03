from tree import TreeNode


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    def search(self, root, val):
        if not root:
            return False
        if root.val == val:
            return True
        return self.search(root.left, val) if val < root.val else self.search(root.right, val)

    def delete(self, root, val):
        if not root:
            return None
        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            if not root.left: return root.right
            if not root.right: return root.left
            node = root.right
            while node.left:
                node = node.left
            root.val = node.val
            root.right = self.delete(root.right, node.val)
        return root

    def inorder(self, node):
        if not node: return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)


bst = BST()
root = None
for val in [5, 3, 7, 2, 4, 6, 8]:
    root = bst.insert(root, val)

print(bst.inorder(root))      # [2, 3, 4, 5, 6, 7, 8]
print(bst.search(root, 4))    # True
root = bst.delete(root, 3)
print(bst.inorder(root))      # [2, 4, 5, 6, 7, 8]
