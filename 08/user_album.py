
def make_album(name, album='L.P', number=''):
    album_list = {}
    polling_active = True
    album_list = {'name':name,'album':album,'number':number}
   #while polling_active = True:
    while polling_active:
        name=input("\nWhat's the name?")
        album=input('\nPlease input the album')
        album_list[name]=name
        album_list[album]=album
        repet = input('\nwould like to quit?')
        if repet == 'quit':
            polling_active = False
        print(album_list)
    return album_list



care=make_album('bqb', 'bb')
print(care)

xiaoxin = make_album('bj')
#print(xiaoxin)

zhu=make_album('zdmx','xzc','8')
print(zhu)

#print (album_list)
#函数里的字典,调用不能用,也就是不能用返回值以外的
#字典是单次的,对于每个参数是独立的
#返回值的用法忘掉了,重新回忆下
#不清字典的话,重复运行会累计,格式也有问题
#n次排错,格式,对齐,开关的写法,还是要多写啊