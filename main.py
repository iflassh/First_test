class Human:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    a = 10

    @property
    def do (self):
        
        return self.name

    @do.setter
    def do (self, name):
        self.name = name

    @do.deleter
    def do (self):
        del self.name

first = Human( 'Alex', 'men', 18)

first.do = 'steve'

