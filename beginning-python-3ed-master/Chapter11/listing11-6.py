'''
要确保文件得以关闭，可使用一条try/finally语句，并在finally子句中调用close。
# 在这里打开文件
try:
# 将数据写入到文件中
finally:
file.close()
实际上，有一条专门为此设计的语句，那就是with语句。
with open("somefile.txt") as somefile:
do_something(somefile)
with语句让你能够打开文件并将其赋给一个变量（这里是somefile）。在语句体中，你将数据
写入文件（还可能做其他事情）。到达该语句末尾时，将自动关闭文件，即便出现异常亦如此。
'''
def process(string):
    print('Processing:',string)




with open('listing11-5.txt') as f:
    char = f.read(1)
    while char:
        process(char)
        char = f.read(1)

print('--------------------------------------------------------------------------')

print('# 使用readline() 迭代行')

with open ('listing11-5.txt') as f2:

    while True:
        chars = f2.readline()
        if not chars:break   #  当 chars 变为空时，chars 为假时，not chars 为真。
        print(chars)

print('--------------------------------------------------------------------------')

print('# 使用readlines() 迭代行')
# 使用readlines 迭代行
with open ('listing11-5.txt') as f3:
    for line in f3.readlines():
        print(line)
