def show_magicians(names):
    '''This function show name from list'''
    for name in names:
        message = "the great :" + name
        print(message)

def make_great(old,new):
    '''plus the great for each element in old list'''
    while old:
        change_one = old.pop()
        change_one = 'the great' + change_one
        new.append(change_one)
        pass

    pass

name_list = ['dwfeb', 'lj', 'bdp']
new_list = []
make_great(name_list, new_list)
show_magicians(new_list)

#忘记加参数,导致报错