class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def minDiffInBST(root: TreeNode) -> int:
    sort = []

    def dps(root: TreeNode):
        if root:
            dps(root.left)
            sort.append(root.val)
            dps(root.right)
    dps(root)
    ans = sort[1] - sort[0]
    for i in range(2,len(sort)):
        temp = sort[i] - sort[i-1]
        if temp < ans:
            ans = temp
    return ans