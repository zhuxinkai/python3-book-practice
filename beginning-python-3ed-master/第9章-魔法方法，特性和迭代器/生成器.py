# encoding = utf-8
'''
 包含 yield 语句的函数被称为生成器 生成器不使用 return 返回一个值，而是可以生成多个值，每次一个。
 每次使用yield 生成一个值后，函数都将冻结，即在此停止执行，等待被重新唤醒。
 被重新唤醒后，函数将从停止的地方开始继续执行。

'''

def flatten(netted):
    for sublist in netted:
        for element in sublist:
            '''
                for num in flatten(nested):
            TypeError: 'int' object is not iterable
            '''
            # return element
            yield element



nested = [[1,2],[3,4],[5]]
for num in flatten(nested):
    print(num)

print('------------------------------------')
print(list(flatten(nested)))
