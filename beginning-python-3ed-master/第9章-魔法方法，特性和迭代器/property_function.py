# encoding = utf-8

class Rectanle():
    def __init__(self):
        self.width = 0
        self.height = 0
    def set_size(self, size):
        self.width,self.height = size

    def get_size(self):
        return self.width,self.height
    size = property(get_size,set_size)

r = Rectanle()
r.height = 100
r.width = 150
print(r.get_size())
print(r.width)
r.set_size((50,20))
print(r.get_size())
# 如你所见，属性size 依然受制于 get_size ,和 set_size 执行的计算，但看起来就像普通属性一样。

r.size = 1,2
print(r.width)





