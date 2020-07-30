class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pathSum(root: TreeNode, sum: int) -> [[int]]:
    if not root:
        return []
    res = []
    def helper(root: TreeNode, sum: int, tmp: [int]):
        if not root.left and not root.right:
            if root.val == sum:
                tmp.append(root.val)
                res.append(tmp)
            return
        if root.left:
            helper(root.left, sum - root.val, tmp+[root.val]) #此处不能为tmp.append(root.val)，因为这种做法引用的是同一个tmp，回溯时修改tmp会出错
        if root.right:
            helper(root.right, sum - root.val, tmp+[root.val])
    helper(root,sum,[])
    return res


def pathSum2(root: TreeNode, sum: int) -> [[int]]:
    res, path = [], []
    def recur(root: TreeNode, tar: int):
        if not root:
            return
        tar -= root.val
        path.append(root.val)
        if tar == 0 and not root.left and not root.right:
            res.append(list(path))
        recur(root.left, tar)
        recur(root.right, tar)
        path.pop()

    recur(root, sum)
    return res


