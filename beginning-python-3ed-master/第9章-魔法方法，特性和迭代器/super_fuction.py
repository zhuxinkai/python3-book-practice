#encoding = utf-8

class Bird():
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("AHAHA........AHAHAH ")
            self.hungry = False
        else:
            print('no ,thank !i amn\'t hungry')


class sing_Bird(Bird):
    def __init__(self):
        # 适用super 更加得直观。
        super().__init__()
        self.sound = 'Squark'
    def sing(self):
        print(self.sound)

oneBird = sing_Bird()
oneBird.eat()
oneBird.eat()
oneBird.sing()


# 对于python 仅要求对象遵循特定得协议。 因此，要称为序列，只需遵循序列协议即可。

