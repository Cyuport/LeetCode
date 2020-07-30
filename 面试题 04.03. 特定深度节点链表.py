class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def listOfDepth(tree: TreeNode) -> [ListNode]:
    ptr = []
    head = []
    def helper(tree: TreeNode, depth: int):
        if not tree:
            return
        if depth > len(ptr):
            new = (ListNode(tree.val))
            ptr.append(new)
            head.append(new)
        else:
            ptr[depth-1].next = ListNode(tree.val)
            ptr[depth-1] = ptr[depth-1].next
        helper(tree.left,depth+1)
        helper(tree.right,depth+1)
    helper(tree,1)
    return head