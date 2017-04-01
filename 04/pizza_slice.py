pizzas = ['Popcorn Shrimp Pizza ', 'Surf&Turf Pizza', 'BBQ Sausage Pizza']
for pizza in pizzas:
    print("I like " + pizza)

print("I really love pizza!")
friend_pizzas = pizzas[:]
pizzas.append('Apple pizza')
print("\nMy favorite pizzas are: ")
for pizza in pizzas:
    print( pizza)

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)