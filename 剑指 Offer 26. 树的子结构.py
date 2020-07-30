class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSubStructure(A: TreeNode, B: TreeNode) -> bool:
    def recur(A: TreeNode, B: TreeNode) -> bool: #判断A树和B树的结构是否完全相同
        if not B:
            return True
        elif not A or A.val != B.val:
            return False
        return recur(A.left, B.left) and recur(A.right, B.right)

    return bool(A and B) and (recur(A, B) or isSubStructure(A.left, B) or isSubStructure(A.right, B))