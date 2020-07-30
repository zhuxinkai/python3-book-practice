# encoding = utf=8


def check_index(key):
    if not isinstance(key,int): raise TypeError
    if key < 0: raise ImportError

class AritheticSequence:
    def __init__(self,start=0,step=1):
        self.start = start
        self.step = step
        self.changed = {}



    def __getitem__(self, key):
        check_index(key)
        try: return self.changed[key]
        except KeyError:
            return self.start + key * self.step



    def __setitem__(self, key, value):
        check_index(key)
        self.changed[key] = value

s = AritheticSequence(1,10)
print(s[4])

# 在这里调用了 __setitme__ 将值对应到相应得索引进行赋值。
s[4] = 2
# 在返回值时，使用try 尝试返回字典值，如果键错误，则生成一个值返回。
print(s[4])

print(s[5])

for i in range(100):
    i +=1
    print(s[i])


# 这个这是一个临时寄存器得方式，所有，没有 DEL    ,因为长度可变，没有len?????,let me try.

class asub(AritheticSequence):
    def __len__(self):
       return len(self)

a = asub(2,3)
print(a[5])
# 没有值，估计还时临时寄存器得情况。。
#print(len(a[5]))

# len ,set ,get ,del 针对可变长 全部支持的协议。 （基本行为，方法） 不可变需要实现两个方法。



class Countlist(list):
    # 初始化的时候，如果没有多个参数的构造，那么无法用range 形成序列。
    def __init__(self,*args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter +=1
        return super(Countlist, self).__getitem__(index)


s = Countlist(range(10))
print(s)
print(s.counter)
s.reverse()
print(s.counter)
s[1] = s[2] + s[3]
print(s.counter)
s[2] = s[5] + s[6]
print(s.counter)