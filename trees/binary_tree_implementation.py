from tree import TreeNode

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_level_order(self, vals):
        # public wrapper
        if not vals:
            self.root = None
            return None
        self.root = self._build(vals, 0)
        return self.root

    def _build(self, vals, i):
        if i >= len(vals) or vals[i] is None:
            return None
        node = TreeNode(vals[i])
        node.left = self._build(vals, 2 * i + 1)
        node.right = self._build(vals, 2 * i + 2)
        return node

    def inorder(self, node):
        if not node:
            return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)

bt = BinaryTree()
bt.insert_level_order([1,2,3,4,5])
print(bt.inorder(bt.root))  # [4, 2, 5, 1, 3]
