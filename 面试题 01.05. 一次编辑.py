def oneEditAway(first: str, second: str) -> bool: #分情况讨论，不优雅
    l1, l2 = len(first), len(second)
    if l1 < l2:
        first, second = second, first
        l1, l2 = l2, l1
    diff = l1 - l2
    if diff > 1:
        return False
    elif diff == 1:
        if l1 * l2 == 0:
            return True
        flag = True
        for i in range(l2):
            if flag: #尚未找到不同字符
                if first[i] != second[i]:
                    flag = False
            else:
                if first[i] != second[i-1]:
                    return False
        if not flag and first[-1] != second[-1]:
            return False
        return True
    else:
        flag = True
        for i in range(l1):
            if first[i] != second[i]:
                if flag:
                    flag = False
                else:
                    return False
        return True

def oneEditAway2(first: str, second: str) -> bool: #前后双指针
    l1, l2 = len(first), len(second)



print(oneEditAway("tea","trea"))