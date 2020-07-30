class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(root: TreeNode) -> bool:
    tmp = []
    def inorder(root: TreeNode):
        if not root:
            return
        inorder(root.left)
        tmp.append(root.val)
        inorder(root.right)
    inorder(root)
    for i in range(1,len(tmp)):
        if tmp[i] <= tmp[i-1]:
            return False
    return True