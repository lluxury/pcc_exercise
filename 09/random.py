from random import randint
# x = randint(1, 6)
# print(x)

# class Die(randint):
#     """docstring for Die"""
#     def __init__(self,number, sides=6):
#         super().__init__(sides)
#         self.number = number
#         self.sides = sides

#     def roll_die(self, number, sides):
#         x = random(self.number,self.sides)
#         print(x)

class Die():
    """docstring for Die"""
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll(self):
        '''roll'''
        return randint(1, self.sides)

# test1 = Die(10, 6)
# test1 = Die(10, 10)
# test1 = Die(10, 20)

#没有模块,未测试 待修正


die = Die()
results = []
for roll_num in range(1000):
    results = die.roll()
    results.append(results)


#貌似和需求不太一样,这个是6面投1000次

