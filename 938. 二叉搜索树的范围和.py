class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def rangeSumBST(root: TreeNode, L: int, R: int) -> int:
    ans = 0
    def dfs(root: TreeNode) -> int:
        global ans
        if root:
            if L <= root.val <= R:
                ans += root.val
            if L <= root.val:
                dfs(root.left)
            if R >= root.val:
                dfs(root.right)
    dfs(root)
    return ans



