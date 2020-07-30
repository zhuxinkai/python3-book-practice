# encoding = utf-8

def flatten(nested):
    try:
        # 不迭代类似于字符串的对象
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            # 递归调用生成器
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


def flatten2(nested):
    for sublist in nested:
        # 递归调用生成器
        for element in flatten(sublist):
            yield element


netsted = ['foo',['bar',['baz']]]
print(list(flatten(netsted)))
print(list(flatten2(netsted)))

netsted2 = [2,3,5,7,5,8,9,10,22,55,66,[[2,4]],'test']
print(list(flatten(netsted2)))






