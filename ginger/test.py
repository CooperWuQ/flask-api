
class Qiyue(object):
    name = 'qiyue'
    age = 18

    def __init__(self):
        self.gender = 'male'

    def keys(self):
        return['name']

    def __getitem__(self,item):
        return getattr(self,item)


o = Qiyue()
print(dict(o))