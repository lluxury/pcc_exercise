squares = []
for value in range(1,11):
    square = value **3
    squares.append(square)

    #print(squares)
print(squares)
#直接逻辑,99乘法表的原理
print("The first three items in the list are: " + str(squares[:3]))
print("Three items from the middle of the list are: " + str(squares[4:7]))
print("The last three items in the list are: " + str(squares[-3:]))