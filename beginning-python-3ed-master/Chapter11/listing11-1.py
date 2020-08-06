# somescript.py


import sys

'''
f = open('listing11-2.txt',"r",encoding="utf-8")
f = open('listing11-3.txt',"w",encoding="utf-8") # 写入模式下打开文件时，既有内容将被删除（截断），
# 如果要在既有文件末尾继续写入，可使用附件模式"wa+"
f = open('listing11-11.txt',"x",encoding="utf-8") # 独占写入模式，文件名不能存在。
f = open('listing11-5.txt',"a",encoding="utf-8")
# 'r+'和'w+'之间有个重要差别：后者截断文件，而前者不会这样做。

f = open('listing11-6.txt',"xb") # 二进制模式，则不能指定文件格式。
f = open('listing11-7.txt',"tw",encoding="utf-8")
f = open('listing11-8.txt',"a+",encoding="utf-8")
# 默认模式为'rt' ,默认使用utf-8编码。
# print(f)

# 如果文件包含非文本的二进制数据，如声音剪辑片段或图像，你肯定不希望执行上述自动转
# 换。为此，只需使用二进制模式（如'rb'）来禁用与文本相关的功能。


for line in f:
    print(line)


print('------------------')
'''

# 计算sys.stdin 中包含有多少个单词的简单脚本。
# 运行方式，在Terminal    type listing11-5.txt | python listing11-1.py
# text = sys.stdin.readlines()
# print(text)

# words = str(text).split()
# wordcount = len(words)
# print('Wordcount:', wordcount)


f = open('listing11-2.txt','r+',encoding='utf-8')

print(f.seek(2))
print(f.read())
print(f.tell())
print(f.seek(0))
print(f.tell())
print(f.read())
print(f.tell())
f.seek(0)
print('-----------------------------------------------')
print(f.readline())
f.seek(0)
print(type(f.readlines())) # 并以列表的方式返回它们  <class 'list'>

f.writelines('this is a write by python \n a another lines') # 方法writelines与readlines相反：接受一个字符串列表
f.seek(0)
print(f.readlines())
f.close() # 对于写入过的文件，一定要将其关闭

