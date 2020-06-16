# Split up a URL of the form http://www.something.com

url = input('Please enter the URL:')
#print(url[3:4])

#增加了对 https 和http两种协议的判断。

if (url[4:5] == 's'):
    domain = url[12:-4]
    domain1 = url[:]
    domain2 = url[-4:]
    domain3 = url[8:11]
else:
    domain = url[11:-4]
    domain1 = url[:]
    domain2 = url[-4:]
    domain3 = url[7:10]

print("Domain name: " + domain)
print("Domain name: " + domain1)
print("Domain name: " + domain2)
print("Domain name: " + domain3)


'''

Please enter the URL:http://www.qq.com
Domain name: qq
Domain name: http://www.qq.com
Domain name: .com
Domain name: www

相应的输出，基本上类似于 urllib.parse.parse (python 2) 中的功能。
不知道源码是否也是类似的采用分片的方式来进行分割和组合。
如果输入的时候带上了https 协议，那么相应的可能产生错误。
在原来基础上增加了判断，是否未https协议。

Please enter the URL:https://www.buhuixiu.com
Domain name: buhuixiu
Domain name: https://www.buhuixiu.com
Domain name: .com
Domain name: /ww


'''