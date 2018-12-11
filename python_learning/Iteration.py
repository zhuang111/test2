from collections import Iterable

"""
    迭代器(Iterator)和可迭代(Iterable)的区别：

    凡是可作用于for循环的对象都是可迭代类型；

    凡是可作用于next()函数的对象都是迭代器类型；

    list、dict、str等是可迭代的但不是迭代器，因为next()函数无法调用它们。可以通过iter()函数将它们转换成迭代器。

    Python的for循环本质上就是通过不断调用next()函数实现的。

"""


# print(isinstance("abc",Iterable)) #字符串可迭代？
# print(isinstance(["2","ds","da"],Iterable)) #列表可迭代？
#
# lis = [1,2,3,5]
#
# it = iter(lis)
#
# print(next(it))
#
# for x in it:
#     print(x)
#
#
# #生成器
# g = (x * x for x in range(1,6))
# print(g)
# print(next(g))
# print(next(g))

#在 Python中，使用yield返回的函数会变成一个生成器（generator）。 在调用生成器的过程中，
# 每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值。并在下一次执行next()方法时从当前位置继续运行。
#斐波那契数列
def fibonacci(n):
    a,b,counter = 1,1,0
    while True:
        if counter > n:
            return
        yield a

        a ,b = b,a+b
        counter +=1

fib = fibonacci(10)
print(type(fib))

for f in fib:
    print(f,end=" ")