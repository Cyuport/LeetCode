def isUnique(astr: str) -> bool:
    #散列表和set为O(n)，但均使用额外数据结构；排序不使用数据结构，但nlogn
    #使用掩码+位运算
    mask = 0
    for c in astr:
        flag = ord(c) - ord('a')
        if mask & 1<<flag:
            return False
        mask |= 1<<flag
    return True

print(isUnique("code"))