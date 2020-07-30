# encoding = utf-8

class Mylass():
    @staticmethod
    def staticmethod1():
        print('this is a static method')

# 装饰器的使用
    @classmethod
    def classmethod1(cls):
        print('this is a class method',cls)



Mylass.staticmethod1()
Mylass.classmethod1()

