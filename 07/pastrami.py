sandwich_orders = ['Bacon','Bacon, egg and cheese','Bagel toast','pastrami','pastrami','pastrami']
print ('pastrami sandwich was sold out')

finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)