# encoding = utf-8
# 关于异常的捕获

while True:
        try:
            print("pls input no 1: ")
            number1 = int(input())

            print("pls input no 2: ")
            number2 = int(input())

            result = number1 / number2
            print(result)
        except Exception as e:
            print("错误的输入：" ,e)
            print('Please try again')
        else:
            break
            # finally 非常适合确保文件或网路套接字等得以关闭。
        finally:
            print("我将关闭文件")


# 可以使用try 方式，来判断，直接对一些类来进行操作。。比如对键值进行操作。
