class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: TreeNode, k: int) -> int:
    stack = []
    count = 0
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        count += 1
        if count == k:
            return root.val
        root = root.right