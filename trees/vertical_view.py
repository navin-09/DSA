
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

def DFS(node,row,col):
    if not node:
        return
    hmap[col].append((row,node.val))
    DFS(node.right,row+1,col-1)
    DFS(node.left,row+1,col+1)


DFS(root,0,0)
res= []

for i in sorted(hmap):
    vals = sorted(hmap[i],key=lambda x: (x[0],x[1]))
    res.append([i[1] for i in vals])

print('-->',res[::-1])
