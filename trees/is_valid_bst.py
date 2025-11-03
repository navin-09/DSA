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

def isValidBST(root) -> bool:
        def helper(root,low, high):
            if not root:
                return True
            if not (low < root.val < high):
                return False
            return helper(root.left, low, root.val) and helper(root.right, root.val,high)
        return helper(root,float('-inf'),float('inf'))

print(isValidBST(root))