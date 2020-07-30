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


print('------------------------------------------------------------')
print("对象，子类的一些内置的函数判断")

print(issubclass(SPAMFilter,Filter))
print(issubclass(mySelf_Filter,Filter))

# “在面向对象设计中，被定义为包含所有实体共性的class类型，被称为“基类”。

print("一个类如果想知道他的基类，可访问其特殊属性__bases__")
print(Filter.__bases__)
print(SPAMFilter.__bases__)

print('----------------------------------------')
print("判断对象是否是特定类的实例，可使用isinstance()")
print(isinstance(s,Filter))
print(isinstance(s,SPAMFilter))
print(isinstance(s,mySelf_Filter))
print('----------------------------------------')
# 如果你要获悉对象属于哪个类，可使用属性 __class__
print("# 如果你要获悉对象属于哪个类，可使用属性 __class__")
print(s.__class__)