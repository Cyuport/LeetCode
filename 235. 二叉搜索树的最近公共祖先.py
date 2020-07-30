class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root == p or root == q:
        return root
    if p.val > q.val:
        p, q = q, p
    if p.val < root.val and q.val > root.val:
        return root
    elif p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left,p,q)
    else:
        return lowestCommonAncestor(root.right,p,q)