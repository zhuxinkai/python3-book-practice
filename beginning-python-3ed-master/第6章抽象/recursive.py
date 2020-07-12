# encoding = utf-8

from functools import reduce

# 阶乘的递归实现 Recursive
print('----------------------------------------------------------------------')
print("阶乘的递归实现")
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)



print(factorial(10))

# 幂的递归实现Recursive
print('-----------------------------------------------------------------------')
print('幂的递归实现Recursive')

def power(x,n):
    if n == 0:
        return 1
    else:
        return x * power(x,n-1)

print(power(3,3))

# 递归，二分法查找。
print('------------------------------------------------------------------------')
print('递归，二分法查找')
def search(squence ,number,lower=0,upper=None):

    if upper == None:
        upper = len(squence) - 1
    if lower == upper:
        # 断言

        assert number == squence[upper]
        return upper
    else:
#   “ / ” 为浮点数除法，返回浮点结果
#
#  “ // ” 表示整数除法，返回不大于结果的一个最大整数
#
# print("6 / 4 =" + str(6 / 4))       //1.5
#  print("6 // 4 =" + str(6 // 4))    //1

        middle = (lower +upper) // 2
        if number > squence[middle]:
            return search(squence,number,middle+1,upper)
        else:
            return search(squence,number,lower,middle)


seq = [37,25,887,26,39,27]
seq.sort()
# seq.sorted 两者的区别在于，sorted 返回一个新的列表。 列表的方法 .sort则是直接对列表进行排序。

print(search(seq,887))

print(search(seq,26))



print("---------------------------------------------------------------------------")

print("函数式编程")

def func(x):
    return x.isalnum()

seq = ["foo","x41","?!","***"]
# filter(func ,seq) 返回一个列表，其中包含对其执行函数的结果返回为真的元素。
print( list(filter(func,seq)))
# map 对序列中的素有元素执行函数
print(list(map(func,seq)))


numberslist = [12,232,4234,123,5435,12312,123,45234,123123,123123,123]
print(sum(numberslist))

print(reduce(lambda x,y:x+y,numberslist))
# apply(func[,args[,kwargs]]) 调用函数（还提供要传递给函数的参数）