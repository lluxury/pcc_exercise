name_list = ['dqx', 'bql', 'xyz', 'txo', 'admin']
    
if name_list:
        #print('We need to find some users!')
    for name in name_list:

        if name == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + name +', thank you for logging in again')
else:
    print('We need to find some users!')

#注意列表的表达方式