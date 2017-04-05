car = 'subaru'
bike = 'bwm'
bake = 'bwm'
print("Is car == 'subaru'? I predict True.")
print(car == bike)
print("\nIs car == 'audi'? I predict False.")
print(car == bake)

car = 'subaru'
bike = 'bwm'
bake = 'Bwm'
print("Is car == 'subaru'? I predict True.")
print(car == bike)
print("\nIs car == 'audi'? I predict False.")
print(bike.lower() == bake.lower())

print(3 == 5)
print(3 != 5)
print(3 > 5)
print(3 < 5)
print(3 >= 5)
print(3 <= 5)   #是一种符号,不是2个条件

print(3 !=5 and 3<=5)
print(3 !=5 or 3>5)

print (3 in [3, 5])
print (3 not in [3, 5])