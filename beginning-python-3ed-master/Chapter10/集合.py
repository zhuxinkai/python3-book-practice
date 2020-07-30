# encoding = utf-8
import os
import math
from functools import reduce

my_sets = []
for i in range(10):
    my_sets.append(set(range(i,i+5)))

'''
实例
合并两个集合，重复元素只会出现一次：
实例 1
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.union(y) 
print(z)
输出结果为：
{'cherry', 'runoob', 'google', 'banana', 'apple'}
'''
# reduce() 函数会对参数序列中元素进行累积。
#
# 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
# 用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
# 得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
print(reduce(set.union,my_sets))

# 集合是可变的。

a = {2,3,45,67}
b = {22,72,36,28,45}
a.add(frozenset(b))
print(a)