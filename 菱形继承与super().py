class A():
    def __init__(self):
        print('enter A')
        print('leave A')


class B(A):
    def __init__(self):
        print('enter B')
        super().__init__()
        print('leave B')


class C(A):
    def __init__(self):
        print('enter C')
        super().__init__()
        print('leave C')


class D(B, C):
    def __init__(self):
        print('enter D')
        super().__init__()
        print('leave D')


d = D()

lst = [1,2,3,4,5]
print(map(lambda x:x**2,[1,2,3,4,5]))
print(lst)


a = [1,2,3]
b = [4,5,6]
zipped = zip(a,b)
print(list(zipped))
print(list(zip(*zipped)))