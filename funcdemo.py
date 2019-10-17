# 沒加小括號: 字典
#   加小括號: 字典[key]
a = print
a(3)

int = print
int("hello")

def test():
    print("hi")

b = test
b()

def test():
    return print

test()("bye")