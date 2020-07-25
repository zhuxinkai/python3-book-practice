# encoding = utf-8
# 超类,指定超类。

class Filter:
    def init(self):
        self.blocked = []
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]



class SPAMFilter(Filter): # SPAMFilter 是Filter 的子类
    def init(self):       # 重写超类Filter 的方法init
        self.blocked = ['SPAM']


f = Filter()
f.init()
print(f.filter([1,2,3]))


s = SPAMFilter()
# 以提供新定义的方式重写Filter 类中方法init 的定义
s.init()
# 直接从Filter 类继承了方法filter 的定义，因此无需重新编写其定义。

class mySelf_Filter(Filter):
    def init(self):
        self.blocked = ['name','age','LOVE']




m = mySelf_Filter()
m.init()
print(m.filter(['SPAM','age','name','hello','SPAM','YOU KNOW THE TRUE','LOVE','SPAM']))




print('创建大量不同的过滤器类，它们从Filter 类派生而来，并且都使用自己编写好的方法filter')
print(s.filter(['SPAM','age','name','hello','SPAM','YOU KNOW THE TRUE','LOVE','SPAM']))


print(issubclass(mySelf_Filter,Filter))