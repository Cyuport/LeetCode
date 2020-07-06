def divingBoard(shorter: int, longer: int, k: int) -> [int]:
    min = k * shorter
    delta = longer - shorter
    ans = []
    if k > 0:
        ans.append(min)
    if delta > 0:
        for i in range(1,k+1):
            ans.append(min+delta*i)
    return ans