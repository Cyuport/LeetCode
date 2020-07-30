import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def rightSideView(root: TreeNode) -> [int]:
    q = collections.deque()
    res = []
    if not root:
        return []
    q.append([root,0])
    while q:
        tmp = q.popleft()
        if not q or q[0][1] > tmp[1]:
            res.append(tmp[0].val)
        if tmp[0].left:
            q.append([tmp[0].left,tmp[1]+1])
        if tmp[0].right:
            q.append([tmp[0].right,tmp[1]+1])
    return res


