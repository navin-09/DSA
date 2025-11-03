from tree import TreeNode


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

def DFS(node):
    if not node:
        return
    DFS(node.right)
    print(str(node.val),end= " ")
    DFS(node.left)

print("inroder", end=" ")
DFS(root)