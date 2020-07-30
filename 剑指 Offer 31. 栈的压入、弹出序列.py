def validateStackSequence(pushed: [int], popped: [int]) -> bool:
    stack = []
    i, j = 0, 0
    while i < len(pushed):
        stack.append(pushed[i])
        i += 1
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    while j < len(popped):
        if stack[-1] != popped[j]:
            return False
        stack.pop()
        j += 1
    return True


print(validateStackSequence([1,2,3,4,5],[4,3,5,1,2]))