#len = len([])

def a():
    len = 1

    def b():
        len = 2
        print(len)

    b()
    print(len)

a()
print(len)


i = 0
#nonlocal无法回溯到global域，因此想修改全局变量的话必须用global，无法用nonlocal
#nonlocal用于修改enclosing（封闭域）的变量；nonlocal会向上回溯到第一层有这个变量的封闭域
def a():
    nonlocal i
    i = 1

    def b():
        i = 2

    b()
    print(i)

a()
print(i)