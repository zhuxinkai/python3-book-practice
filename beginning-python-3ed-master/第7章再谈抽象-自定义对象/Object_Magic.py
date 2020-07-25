# encoding = utf-8
# 多态： 对不同类型的对象执行相同的操作， 而这些操作就像“ 被施了魔法” 一样能够正常运行。
# 封装： 对外部隐藏有关对象工作原理的细节。
# 继承 ： 可基于通用类创建出专用类。

# 多态函数举例：
print("-----------------------------------------------------------")
print("多态函数举例：")
print("支持多种数据类型，对象的处理")

def length_message(x):
    print("The length of",repr(x),"is",len(x))

length_message([1,2,3,45])

length_message("the new world")



