from Restaurant import Restaurant


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

# my_icecreamstand=IceCreamStand('bsk','pizza')
# my_icecreamstand.IceCreamStand()

#不是入口的参数如何关联,待解决, TypeError: 'str' object is not callable