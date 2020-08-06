def process(line):
    print('Proceesing :' , line)


# 使用readlines 占用大量的内存。
# while readline 方式，但是首选用for 循环
# 用fileinput 的方式，延迟行迭代的方法--说它延迟只是它只读取世界需要的文本部分。


import fileinput
for line in fileinput.input('listing11-11.txt'):
    process(line)


