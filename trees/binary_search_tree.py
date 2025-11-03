from tree import TreeNode

root = TreeNode(8)

root.left = TreeNode(4,
    TreeNode(2),
    TreeNode(6, TreeNode(5))
)

root.right = TreeNode(12,
    TreeNode(10),
    TreeNode(14, TreeNode(13), TreeNode(15))
)

def bst(node):
    if not node: return
    bst(node.left)
    print(str(node.val),end= " ")
    bst(node.right)


bst(root)