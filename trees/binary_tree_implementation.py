class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_level_order(self, vals):
        from collections import deque
        if not vals: return None
        self.root = TreeNode(vals[0])
        queue = deque([self.root])
        i = 1
        while i < len(vals):
            node = queue.popleft()
            if vals[i] is not None:
                node.left = TreeNode(vals[i])
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] is not None:
                node.right = TreeNode(vals[i])
                queue.append(node.right)
            i += 1
        return self.root

    def inorder(self, node):
        if not node: return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)

bt = BinaryTree()
bt.insert_level_order([1, 2, 3, 4, 5])
print(bt.inorder(bt.root))  # [4, 2, 5, 1, 3]
