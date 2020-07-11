class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedArrayToBST(nums: [int]) -> TreeNode:
    n = len(nums)
    if not n:
        return None
    root = TreeNode(nums[n//2])
    if n > 1:
        root.left = sortedArrayToBST(nums[:n//2])
        root.right = sortedArrayToBST(nums[n//2+1:])
    return root