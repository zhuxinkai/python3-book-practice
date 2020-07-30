# encoding =utf-8

print(" 多个超类")

class Super1:
    def cacl(self,expression):
        self.value = eval(expression)

class Super2:
    def show(self,expression):
        print(expression+'计算结果是',self.value)


class result(Super1,Super2):
    pass

s = result()
s.cacl('2 + 1 * 3')
s.show('2 + 1 * 3')


# 多重继承，是一个功能强大的工具。但是，不推荐使用，因为使用过程中，可能会产生某些意想不到的“并发症”



# MRO 方法解析顺序

print('# MRO 方法解析顺序')
# 如果存在多个超类，多个超类中存在又同名方法的时候，存在哪个超类的哪个方法被优先执行的问题。
# 优先的顺序是，看定义子类的时候，超类的排名。 。 result (Super1,Super2)  其中Super1 中方法的比Super2中的同名方法优先被调用执行。  如果 result(Super2, Super1)则相反。


