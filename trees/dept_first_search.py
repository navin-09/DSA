
from binary_search_tree import TreeNode


root = TreeNode(8)

root.left = TreeNode(4,
    TreeNode(2),
    TreeNode(6, TreeNode(5))
)

root.right = TreeNode(12,
    TreeNode(10),
    TreeNode(14, TreeNode(13), TreeNode(15))
)

def DFS(node):
    if not node:
        return
    print(str(node.val),end= " ")
    DFS(node.right)
    DFS(node.left)


DFS(root)