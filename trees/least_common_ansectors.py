
from tree import TreeNode


# ---------- Build Test Tree ----------
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

p = root.left.left       # Node 6
q = root.left.right      # Node 2



def findPath(node, target, path):
    if not node:
        return False
    path.append(node)
    if node == target:
        return True
    if findPath(node.left, target, path) or findPath(node.right, target, path):
        return True
    path.pop()  # backtrack if target not found
    return False


# ---------- Run ----------
ppath, qpath = [], []
findPath(root, p, ppath)
findPath(root, q, qpath)

lca = None
for i, j in zip(ppath, qpath):
    if i == j:
        lca = i

print("LCA =", lca.val if lca else None)
