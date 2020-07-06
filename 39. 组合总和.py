def combinationSum(candidates: [int], target: int) -> [[int]]:
    if not candidates:
        return []
    n = len(candidates)
    candidates.sort()
    res = []
    def helper(i, tmp, target):
        if target == 0:
            res.append(tmp)
            return
        if i == n or candidates[i] > target or target < 0:
            return
        helper(i, tmp+[candidates[i]], target-candidates[i])
        helper(i+1, tmp, target)
    helper(0, [], target)
    return res

def combinationSum2(candidates: [int], target: int) -> [[int]]:
    if not candidates:
        return []
    n = len(candidates)
    candidates.sort()
    res = []
    def helper(i, tmp, target):
        if target == 0:
            res.append(tmp)
            return
        if i == n or candidates[i] > target:
            return
        helper(i+1, tmp+[candidates[i]], target-candidates[i])
        j = i + 1
        flag = False
        for j in range(i+1, n):
            if candidates[j] != candidates[i]:
                flag = True
                break
        if flag:
            helper(j, tmp, target)
    helper(0, [], target)
    return res

if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(combinationSum2(candidates,target))