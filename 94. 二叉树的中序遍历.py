class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(root: TreeNode) -> [int]:
    if not root:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)