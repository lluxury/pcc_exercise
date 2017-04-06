numbers = list(range(1,10))
    
if numbers:
        #print('We need to find some users!')
    for number in numbers:

        if int(number) ==  1:
            print(str(number) + 'st')
        elif int(number) ==  2:
            print( str(number)  +'nd')
        else:
            print( str(number)  +'st')
else:
    print('We need to find some users!')

#注意数列的生成方法