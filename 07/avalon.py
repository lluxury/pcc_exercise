avalons = {}

polling_active = True

while polling_active:
    name = input('\n What is your name')
    response = input('Where is your avalon')

    avalons['name'] = response

    repeat = input('Would you like to let another person respond? (yes/no)')
    if repeat == 'no':
        polling_active = False

for name, response in avalons.items():
    print(name + ' would you like to ' + response + '.')



    pass

#输入要放循环里面,开关放里面,添加字典也放里面,换言之,要有中断