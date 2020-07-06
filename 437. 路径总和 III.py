class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pathSum(root: TreeNode, sum: int) -> int:
    if not root:
        return 0
    if root.val == sum:
        return 1 + pathSum(root.left, 0) + pathSum(root.right, 0)
    return pathSum(root.left, sum - root.val) + pathSum(root.right, sum - root.val) + pathSum(root.left, sum) + pathSum(root.right, sum)