def demo(*args):
    print(*args)


demo('a','b','c','d', 1, 2, 3)


def demo2(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

demo2(name='abc',age=12)