# encoding = utf-8

f= open('listing11-4.txt','w')

f.write('Hello, ')
# print(f.read())  io.UnsupportedOperation: not readable 如果文件没有关闭，那么不可对其进行读操作。
f.close()
f = open('listing11-4.txt','r+')
print(f.read(3))

# 'r+'和'w+'之间有个重要差别：后者截断文件，而前者不会这样做。
f2= open('listing11-5.txt','r')
print(f2.read())