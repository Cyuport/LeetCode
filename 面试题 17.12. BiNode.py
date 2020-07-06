class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def convertBiNode(root: TreeNode) -> TreeNode:
    if root is None:
        return None
    head, tail = help(root)
    return head

def help(root: TreeNode):
    head,tail = root, root
    if root.left:
        lhead,ltail = help(root.left)
        head = lhead
        ltail.right = root
    if root.right:
        rhead,rtail = help(root.right)
        tail = rtail
        root.right = rhead
    root.left = None
    return head,tail