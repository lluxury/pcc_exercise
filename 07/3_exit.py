prompt = "\nWhat is your age "
prompt += "\nEnter 'quit' to end of program."
messeage = ""
active = True
while active:
    messeage = input(prompt)
    #print("We will add "+ messeage + " with you pizza")
    if int(messeage) < 3:
        print('you are free')
        active = False
    elif int(messeage) < 12 and int(messeage) >=3:
        print('Fare 10')
        break
    else:
        print('Fare 15')

#严格对齐,没有while也能用,但要调整格式