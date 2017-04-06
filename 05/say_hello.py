name_list = ['dqx', 'bql', 'xyz', 'txo', 'admin']
for name in name_list:
    if name == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello ' + name +', thank you for logging in again')