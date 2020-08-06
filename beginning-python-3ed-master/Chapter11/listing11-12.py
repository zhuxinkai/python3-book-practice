
# 文件实际上时可迭代的，这意味着可在for 循环中直接使用它们来迭代行。
import sys

def process(line):
    print('Processing:' , line)


with open('listing11-11.txt') as f:
    for line in f:
        process(line)


print('----------------------------------------------------------')
print("在不将文件对象赋予给变量的情况下迭代文件")
for line in open('listing11-11.txt'):
    process(line)

print('----------------------------------------------------------')
print("使用stdin 方式，sys.stdin 也是可迭代的")
# 使用stdin 的方式需要将文件 cat ,或者type 到其管道。
for line in sys.stdin:
    process(line)
