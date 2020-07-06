class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrder(root: TreeNode) -> [[int]]:
    if not root:
        return []
    l = levelOrder(root.left)
    r = levelOrder(root.right)
    ll, lr = len(l), len(r)
    ans = [l[i] + r[i] for i in range(min(ll, lr))]
    if len(l) > len(ans):
        ans += [l[i] for i in range(len(ans), ll)]
    if len(r) > len(ans):
        ans += [r[i] for i in range(len(ans), lr)]
    ans.insert(0, [root.val])
    return ans


if __name__ == '__main__':
    l, r = [2], []
    ans = [l[i] + r[i] for i in range(min(len(l), len(r)))]
    print("ans=",ans)
    if len(l) > len(ans):
        ans += [l[i] for i in range(len(ans), len(r))]
    if len(r) > len(ans):
        ans += [r[i] for i in range(len(ans), len(r))]
    print(ans)