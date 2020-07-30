import sys
def view(n: int, h: [int]) -> [int]:
    v = []
    right, left = [0]*n, [0]*n
    stack_r, stack_l = [], []
    for i in range(n-1,-1,-1): #向右看
        right[i] = len(stack_r)
        if i == n-1:
            stack_r.append(h[i])
        elif h[i]<stack_r[-1]:
            stack_r.append(h[i])
        else:
            while len(stack_r) and h[i]>=stack_r[-1]:
                stack_r.pop()
            stack_r.append(h[i])

    for i in range(n):
        left[i] = len(stack_l)
        if i == 0:
            stack_l.append(h[i])
        elif h[i]<stack_l[-1]:
            stack_l.append(h[i])
        else:
            while len(stack_l) and h[i]>=stack_l[-1]:
                stack_l.pop()
            stack_l.append(h[i])


    for i in range(n):
        v.append(left[i]+right[i]+1)
    return v


for line in sys.stdin:
    a = line.split()
    h = []
    for i in range(1,len(a)):
        h.append(a[i])
    v = view(a[0],h)
    for i in range(len(v)):
        print(v[i],end='')
        if i != len(v)-1:
            print(' ',end='')