prompt = "\nWhat is your age "
prompt += "\nEnter 'quit' to end of program."
messeage = ""
while messeage !='quit':
    messeage = input(prompt)
    #print("We will add "+ messeage + " with you pizza")
    if int(messeage) < 3:
        print('you are free')
    elif int(messeage) < 12 or int(messeage) >=3:
        print('Fare 10')
    else:
        print('Fare 15')

#严格对齐,没有while也能用,但要调整格式