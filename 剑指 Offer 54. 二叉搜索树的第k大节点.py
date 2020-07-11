class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def kthLargest(root: TreeNode, k: int) -> int:
    nums = []
    def dfs(root: TreeNode):
        if not root:
            return
        dfs(root.left)
        nums.append(root.val)
        dfs(root.right)
    dfs(root)
    begin, end = 0, len(nums)-1
    mid = (begin + end)//2
    k = len(nums)-k
    while mid != k:
        if mid > k:
            end = mid
        else:
            if begin == mid:
                begin += 1
            else:
                begin = mid
        mid = (begin + end)//2
    return nums[mid]
