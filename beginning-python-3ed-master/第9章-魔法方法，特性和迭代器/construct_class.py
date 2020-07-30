# encoding = utf-8

__metaclass__ = type

# 构造函数

class FooBar:
    def __init__(self,value=42):
        self.somevar = value


s =  FooBar()
print(s.somevar)
s = FooBar('This is a constructor argument')
print(s.somevar)

# 在所有的python 魔法中，__init__绝对是你用得最多得。



class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaa......')
            self.hungry = False
        else:
            print("no ,thanks ,i 's not hungry")


greenbird = Bird()
greenbird.eat()
greenbird.eat()


class singBrid(Bird):
    def __init__(self):
        self.sound = 'Squawk'
    def sing(self):
        print(self.sound)

yellowbird = singBrid()
yellowbird.sing()
'''

   if self.hungry:
AttributeError: 'singBrid' object has no attribute 'hungry'
'''

#yellowbird.eat()


class singBrid2(Bird):
    def __init__(self):
        # 调用未关联得超类构造函数。
        Bird.__init__(self)
        self.sound = 'Squawk'
    def sing(self):
        print(self.sound)

whitebird = singBrid2()
whitebird.eat()
whitebird.eat()