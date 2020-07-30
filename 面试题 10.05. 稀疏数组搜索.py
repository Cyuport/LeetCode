def findString(words: [str], s: str) -> int:
    i, j = 0, len(words)-1
    while i <= j:
        mid = (i+j)>>1
        tmp = mid
        while words[mid] == '' and mid < j:
            mid += 1
        if words[mid] == '':
            j = tmp-1
            continue
        if words[mid] == s:
            return mid
        elif words[mid] < s:
            i = mid+1
        else:
            j = mid-1
    return -1
