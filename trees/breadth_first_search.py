
from collections import defaultdict
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

hmap = defaultdict(list)

def DFS(node,level):
    if not node:
        return
    hmap[level].append(node.val)
    DFS(node.right,level+1)
    DFS(node.left,level+1)


DFS(root,0)
print(hmap)