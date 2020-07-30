class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrder(root: TreeNode) -> [[int]]:
    res = []
    if not root:
        return res
    def helper(root: TreeNode, depth: int):
        if not root:
            return
        if depth >= len(res):
            res.append([])
        res[depth].append(root.val)
        helper(root.left,depth+1)
        helper(root.right,depth+1)
    helper(root,0)
    for i in range(len(res)):
        print(res[i])
        if i%2:
            res[i]=res[i][-1::-1]
    return res



