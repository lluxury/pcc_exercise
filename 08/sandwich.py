def sandwich_list(*names):
    '''This function show name from list'''
    print('sandwich list')
    for name in names:
        print(name)
    print('\n')

sandwich_list('pg')
sandwich_list('egg','pg')
sandwich_list('egg','pg','tomato')

