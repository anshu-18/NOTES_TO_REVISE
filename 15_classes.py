class Point:
    def __init__(self, x, y):  #constuctor
        self.x_ = x
        self.y_ = y

    def get(self):
        print('Getting the value')

    def set_(self, val):
        self.y_ = val

p1 = Point(23, 12)
print(p1.y_)
p1.set_(30)
print(p1.y_)

#p2 = Point()
#print(p2.y_)

#PERSON CLASS
class Person:
    def __init__(self,talk):
        self.talk_ = talk

    def is_talking(self):
        print(f'talk value {self.talk_}')
        if self.talk_ == 'yes':
            print('hey!! I am talking!!!')
        else:
            print('not talking')

pn1 = Person('yes')
pn1.is_talking()
pn1.talk_ = 'no'
pn1.is_talking()