# encoding=utf-8



def lookup(data,lable,name):
    return (data[lable].get(name));


def store(data,full_name):
    names= full_name.split()
    if len(names) == 2: names.insert(1,' ')
    labels = ['first','middle','last']

    for label,name in zip(labels,names):
        people = lookup(data,label,name)
        print(people is data[label].get(name) )
        if people:

          # 为什么people.append 直接影响到了data中的数据？
          # 因为返回的是列表，也就是对包含字典data 进行了修改。
         people.append(full_name)

        else:
         # 这里，必须将full_name 转成列表，而不能直接用字符串赋值。
            data[label][name] = [full_name]



def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


MyNames = {}
init(MyNames)
store(MyNames,'Maguns Lie Hetland')
store(MyNames,'Annie Lie Hetland')
print(MyNames)

