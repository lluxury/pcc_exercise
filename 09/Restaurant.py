class Restaurant():
    """docstring for Restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        #super(Restaurant, self).__init__()
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_user(self):
        '''模拟小狗被命令时蹲下'''
        print(" The name of restaurant is " + self.restaurant_name.title())
        print(" The type of restaurant is " + self.cuisine_type.title())

    def open_restaurant(self):
        '''模拟小狗被命令打滚'''
        print(self.restaurant_name.title() + " is opening")
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