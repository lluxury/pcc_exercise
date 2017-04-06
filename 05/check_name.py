current_users = ['dqx', 'bql', 'xyz', 'txo', 'admin']
new_users = ['dqx', 'bql', 'xyz1', 'txo', 'admin']
    
if new_users:
        #print('We need to find some users!')
    for new_user in new_users:

        if new_user.lower() in  current_users:
            print(new_user + ' is exist')
        else:
            print('Hello ' + new_user +', is avilable')
else:
    print('We need to find some users!')

#注意列表的表达方式