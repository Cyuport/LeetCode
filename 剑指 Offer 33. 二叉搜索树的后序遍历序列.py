def verifyPostorder(postorder: [int]) -> bool: #先判断能否分出左右子树，再分别递归左右子树
    if len(postorder) <= 1:
        return True
    l, r = 0, len(postorder)-2
    root = postorder[-1]
    while postorder[l] < root:
        l += 1
    while postorder[r] > root:
        r -= 1
    if r + 1 != l:
        return False
    return verifyPostorder(postorder[:l]) and verifyPostorder(postorder[l:-1])


print(verifyPostorder([1,3,2,6,5]))
