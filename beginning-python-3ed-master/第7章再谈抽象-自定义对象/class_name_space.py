# encoding = utf-8
class MemberCounter:
    # 在类的作用域下定义了一个变量，所有的实例都可以访问它，通过既定的方法操作它。
    member = 0

    def init(self):
        MemberCounter.member += 1


m1 = MemberCounter()
m1.init()
print(MemberCounter.member)
print('--------------------------------------------------------------------------------------------------')
m2 = MemberCounter()
m2.init()
print(MemberCounter.member)
print('---------------------------------------------------------------------------------------------------')
print(m1.member)
print(m2.member)
print(MemberCounter.member)
print('--------------------------------------------------------------------------------------------------')
# m1 的一个属性，这个属性遮住了类级变量。 类级变量 MemberCounter.member  .
print(" m1 的一个属性，这个属性遮住了类级变量。 类级变量 MemberCounter.member  .")
print("给对象M1的空间 里的member 赋值 tony")
m1.member = 'tony'
print(MemberCounter.member)
print("打印m1对象中的member的值：   ")
print(m1.member)
print("打印m2 对象中的member 的值：   ")
print(m2.member)
