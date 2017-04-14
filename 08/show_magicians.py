def show_magicians(names):
    '''This function show name from list'''
    for name in names:
        message = "the great :" + name
        print(message)


name_list = ['dwfeb', 'lj', 'bdp']
show_magicians(name_list)

#忘记加参数,导致报错