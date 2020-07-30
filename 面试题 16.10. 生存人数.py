def maxAliveYear(birth:[int], death:[int]) -> int:
    birth = sorted(birth)
    death = sorted(death)
    i, j = 0, 0
    maxYear = birth[0]
    count = 0
    tmp = 0
    while i<len(birth):
        if birth[i] <= death[j]:
            count += 1
            if count > tmp:
                tmp = count
                maxYear = birth[i]
            i += 1
        else:
            count -= 1
            j += 1
    return maxYear
