# encoding = utf-8
import os

print(os.environ['PYTHONPATH'])

'''
请注意，这里用引号将Program Files和Mozilla Firefox括起来了。如果不这样做，底层shell
将受阻于空白处（对于PYTHONPATH中的路径，也必须这样做）。另外，这里必须使用反斜杆，因
为Windows shell 无法识别斜杠。如果你执行这个命令， 将发现浏览器试图打开名为
Files"\Mozilla…（空白后面的命令部分）的网站。另外，如果你在IDLE中执行这个命令，将出
现一个DOS窗口，关闭这个窗口后浏览器才会启动。总之，结果不太理想。
'''



# os.system(r'C:\"Program Files (x86")\"5211game"\11Loader.exe')

#另一个函数更适合用于完成这项任务，它就是Windows特有的函数os.startfile。

os.startfile(r'C:\Program Files (x86)\5211game\11Loader.exe')

