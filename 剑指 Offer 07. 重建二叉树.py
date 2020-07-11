class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder: [int], inorder: [int]) -> TreeNode:
    n = len(preorder)
    if not n:
        return None
    val = preorder[0]
    pos = 0
    for i in range(n):
        if inorder[i] == val:
            pos = i
            break
    root = TreeNode(val)
    root.left = buildTree(preorder[1:1+pos], inorder[:pos])
    root.right = buildTree(preorder[1+pos:], inorder[pos+1:])
    return root

