#encoding=utf-8

def in_the_middle(x,*y,z):
    print(x,y,z)


in_the_middle(1,2,3,4,5,6,7,z=8)




def story(**kwds):
    return 'Once upon a time, there was a '\
        '{job} called {name}.'.format_map(kwds)

print(story(name='zhuxinkai',job='information security engineer'))

parmas = {'job':'language','name':'python'}
print(story(**parmas))


print("--------------------------------------------------------")
del parmas['job']
print(story(job='stroke of genius',**parmas))
print("--------------------------------------------------------")


def power(x,y,*others):
    if others:
        print('Received redundant parameters:',others)
    return pow(x,y)

print (power(2,3))

print (power(3,2))
# 这里的 （5，） * 2 则是把5复制两遍
parmas2 = (5,) * 2
print(power(*parmas2))
print(power(5,5))
print(power(3,3,"hello world"))

print("---------------------------------------------------------")
# 这是一个步长行函数的源码
def interval(start, stop=None,step=1):
    'Imitates range() for step > 0'
    if stop is None:
        # 等于start = 0 ,stop = start
        start,stop = 0,start

    result = []


    i = start
    while i < stop:
        result.append(i)
        i += step
    return result


print(interval(10))
print(interval(1,5))
print(interval(3,12,4))
print(power(*interval(3,7)))