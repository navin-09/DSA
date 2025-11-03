class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

def DFS(node):
    if not node:
        return
    print(str(node.val),end= " ")
    DFS(node.right)
    DFS(node.left)


DFS(root)