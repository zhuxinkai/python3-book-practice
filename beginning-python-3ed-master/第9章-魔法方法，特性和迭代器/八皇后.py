# encoding = utf-8
'''
这是一个典型的回溯问题：在棋盘的第一行尝试为第一个皇后选择一个位置，再在第二行尝
试为第二个皇后选择一个位置，依次类推。在发现无法为一个皇后选择合适的位置后，回溯到前
一个皇后，并尝试为它选择另一个位置。最后，要么尝试完所有的可能性，要么找到了答案。
在前面描述的问题中，只有8个皇后，但这里假设可以有任意数量的皇后，从而更像现实世
界的回溯问题
'''

'''
 魔法方法：Python中有很多特殊方法，其名称以两个下划线开头和结尾。这些方法的功能
各不相同，但大都由Python在特定情况下自动调用。例如__init__是在对象创建后调用的。

 构造函数：很多面向对象语言中都有构造函数，对于你自己编写的每个类，都可能需要
为它实现一个构造函数。构造函数名为__init__，在对象创建后被自动调用。

 重写：类可重写其超类中定义的方法（以及其他任何属性），为此只需实现这些方法即可。
要调用被重写的版本，可直接通过超类调用未关联版本（旧式类），也可使用函数super
来调用（新式类）。

 序列和映射：要创建自定义的序列或映射，必须实现序列和映射协议指定的所有方法，
其中包括__getitem__和__setitem__等魔法方法。通过从list（或UserList）和dict（或
UserDict）派生，可减少很多工作量。

 迭代器：简单地说，迭代器是包含方法__next__的对象，可用于迭代一组值。没有更多的
值可供迭代时，方法__next__应引发StopIteration异常。可迭代对象包含方法__iter__，
它返回一个像序列一样可用于for循环中的迭代器。通常，迭代器也是可迭代的，即包含
返回迭代器本身的方法__iter__。

 生成器：生成器的函数是包含关键字yield的函数，它在被调用时返回一个生成器，即一
种特殊的迭代器。要与活动的生成器交互，可使用方法send、throw和close。



'''

def conflict(state,nextX):
        nextY = len(state)
        for i in range(nextY):
            if abs(state[i] - nextX) in (0, nextY - i):
                return True
        return False

'''
def queens(num,state):
    if len(state) == num-1:
        for pos in range(num):
            if not conflict(state,pos):
                yield pos



print(list(queens(4,(1,3,0))))
'''

def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state,pos): # 校验位置是否冲突，not conflict 则为不冲突。
            if len(state) == num -1:
                yield (pos,)
            else:
                for result in queens(num,state+(pos,)):
                    yield (pos,) + result

print(len(list(queens(8))))

def prettyprint(solution):
    def line(pos,length = len(solution)):
        return '.' *(pos) + 'X' +'.' *(length-pos-1)
    for pos in solution:
        print(line(pos))


import random
prettyprint(random.choice(list(queens(8))))

