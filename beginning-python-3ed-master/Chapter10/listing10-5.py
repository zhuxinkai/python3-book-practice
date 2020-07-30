# reverseargs.py
import copy
import sys
'''
__all__ 的方式，可以屏蔽其下面的方法或者变量。 如果需要导入，则需要显示导入。 from copy import PyStringMap
如果没有__all__ , 使用from copy import * 的方式，则会导入所有不以下划线打头的全局名称。

'''
args = sys.argv[1:]
args.reverse()
print(' '.join(args))

for n in dir(copy):
    print(n)
    if not n.startswith('__'):
        print(n)

print(copy.__all__)

'''
>>> help(copy.copy)
Help on function copy in module copy:

copy(x)
    Shallow copy operation on arbitrary Python objects.

    See the module's __doc__ string for more info.


'''

print(copy.copy.__doc__)

print(copy.__file__)  # C:\Program Files\Python38\lib\copy.py



for x in dir(sys):
    print(x)
print(help(sys.argv))




