class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeToDoublyList(root: Node) -> Node:
    def dfs(cur: Node):
        if not cur:
            return
        dfs(cur.left)
        global pre,head
        if pre:
            pre.right, cur.left = cur, pre
        else:
            head = cur
        pre = cur
        dfs(cur.right)

    if not root:
        return
    pre = None
    dfs(root)
    head.left, pre.right = pre, head
    return head
