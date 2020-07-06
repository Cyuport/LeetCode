class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


def sortedArrayToBST(nums: [int]) -> TreeNode:
    def helper(left: int, right: int) -> TreeNode:
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = helper(left, mid-1)
        root.right = helper(mid+1,right)
        return root
    return helper(0,len(nums)-1)
