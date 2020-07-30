# numberlines.py
# rstrip()delete string chars at the end of string.（default is blank）
import fileinput

for line in fileinput.input(inplace=False):
    line = line.rstrip()
    # 获取行号
    num  = fileinput.lineno()
    '''
    ^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。

+ 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格

b、d、o、x 分别是二进制、十进制、八进制、十六进制。

此外我们可以使用大括号 {} 来转义大括号，如下实例：
    
    
    '''

    print('{:<50} # {:2d}'.format(line, num))
    #print(line+'   #  '+str(num))


