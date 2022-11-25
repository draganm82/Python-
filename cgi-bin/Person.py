class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    def lastName (self):
        return self.name.split() [-1]
    def giveRise (self, percent):
        self.pay*=(1.0+percent)
    def giveFall (self,percent):
        self.pay *=(1.0 - percent)
if __name__ =='__main__':
    bob=Person('Bob Smith', 42, 30000, 'software')
    sue = Person ('Sue Jones', 45, 40000, 'hardware')
    print(bob.name, sue.name, sue.pay, bob.pay)

    print(bob.lastName())
    sue.giveRise(.10)
    print(sue.name, sue.age, sue.pay)
    bob.giveRise(.20)
    print (bob.name, bob.pay, bob.pay)

