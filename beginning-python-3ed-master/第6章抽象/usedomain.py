# encoding=utf-8


# 全局变量 ，局部变量

# 像这样访问全局变量是众多bug根源，务必慎用全局变量。尽量不要在

def combin(parames):
    print(parames + outsidevalue)

outsidevalue = 'susan'

combin('i love ')

print("-------------------------------------------------------------------")

# 如果一个局部变量或者参数于你访问的全局变量同名，就无法直接访问全局变量。

x = 1

def change_gloabal():
    global x
    x+=1

change_gloabal()

print(x)

print("--------------------------------------------------------------------")

# 作用域嵌套

def multiplier(factor):
    # 像 mutiplierbyfactory 这样存储其所在作用域的函数称为闭包
    def mutiplierbyfactory(number):
        return number * factor
    return mutiplierbyfactory

# <function multiplier.<locals>.mutiplierbyfactory at 0x000001A45CC82940>

double = multiplier(3)
print(double(5))

