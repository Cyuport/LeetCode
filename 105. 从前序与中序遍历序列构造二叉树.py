class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(preorder: [int], inorder: [int]) -> TreeNode:
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    root_index = inorder.index(root)
    root.left = buildTree(preorder[1:root_index + 1], inorder[0:root_index])
    root.right = buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
    return root