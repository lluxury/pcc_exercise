sandwich_orders = ['Bacon','Bacon, egg and cheese','Bagel toast']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print ("I made your " + sandwich + " sandwich")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(sandwich)