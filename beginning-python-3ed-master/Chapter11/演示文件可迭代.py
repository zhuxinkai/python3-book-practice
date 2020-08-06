# encoding = utf-8

f = open('listing11-12.txt','w')
print('first','line' ,file=f)
print('second','line',file=f)
print('thrid','line','finally',file=f)

f.close()

lines = list(open('listing11-12.txt'))
print(lines)


first ,second,thrid = open('listing11-12.txt')
print(first)
print(second)
print(thrid)