# encoding=utf-8
# 7.2.4 再谈隐藏


class Secretive:

 # 这样的方法类似于其他语言的标准私有方法。
    def __inaccessible(self):
        print("Bet you can't see me......")

    def accessible(self):
        print("The secret message is :")
        self.__inaccessible()


s = Secretive()
s.accessible()

# 处理方法并不标准， 在所有以两个下划线打头的名称都进行转换，即在开头加上一个下划线和类名。
# 总之，你无法禁止别人访问对象的私有方法和属性。
# 可以采用__ 双下划线打头的方式，发出一种信号，不要从外部修改属性或方法的信号。 同时 from module import * 不会导入以一个下划线打头的名称。


s._Secretive__inaccessible()

