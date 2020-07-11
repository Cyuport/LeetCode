class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mirrorTree(root: TreeNode) -> TreeNode:
    if not root:
        return
    temp = root.left
    root.left = mirrorTree(root.right)
    root.right = mirrorTree(temp)
    return root
