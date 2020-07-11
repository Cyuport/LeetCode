class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root: TreeNode) -> [[int]]:
    if not root:
        return []
    res = []

    def bfs(root: TreeNode, level: int):
        if not root:
            return
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        bfs(root.left, level + 1)
        bfs(root.right, level + 1)

    bfs(root, 0)
    return res