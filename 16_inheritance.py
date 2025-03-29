import random

class Play:
    def __is_playing(self): #private method
        print('I am playing a game')

class Dice(Play):
    def __init__(self, num):
        self.num = num
    def roll(self):
        self._Play__is_playing()
        print(f'({random.choice(self.num)}, {random.choice(self.num)})')

num=[1,2,3,4,5,6]
d1=Dice(num)
d1.roll()