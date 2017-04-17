class Restaurant():
    """固定的值在函数入口的参数里没有"""
    def __init__(self, restaurant_name, cuisine_type):
        #super(Restaurant, self).__init__()
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_user(self):
        '''描述'''
        print(" The name of restaurant is " + self.restaurant_name.title())
        print(" The type of restaurant is " + self.cuisine_type.title())

    def open_restaurant(self):
        '''欢迎'''
        print(self.restaurant_name.title() + " is opening")
        pass
    
    def set_number_served(self, number):
        self.number_served = number
        print(self.number_served)

    def increment_number_served(self,plus):
        #self.number_served += self.increment_number_served(plus)
        self.number_served += plus
        #print(self.number_served)

    def read_number(self):
        print(self.number_served)
        pass



my_Restaurant=Restaurant('weilian', '6')
print ("my Restaurant's restaurant_name is " + my_Restaurant.restaurant_name.title())
print ("my Restaurant's cuisine_type is " + my_Restaurant.cuisine_type.title())
my_Restaurant.describe_user()
my_Restaurant.open_restaurant()

my_Restaurant2 = Restaurant('kfc', 'fastfood')
my_Restaurant2.describe_user()

my_Restaurant3 = Restaurant('Mc_donalds', 'fastfood')
my_Restaurant3.describe_user()

my_Restaurant.set_number_served(9)
my_Restaurant.increment_number_served(18)
my_Restaurant.read_number()

#函数的操作要通过函数调用,读,改