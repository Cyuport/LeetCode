lis = [1,2,3,4,5]

def fn(x):
    return x**2

res = map(fn, lis)

print(res)

res = [i for i in res]
print(res)

