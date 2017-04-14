
def make_album(name, album='China'):
    album_list = {name:album}
    print (album_list)
    return album_list

care=make_album('bqb', 'bb')
print(care)

xiaoxin = make_album('bj')
#print(xiaoxin)

zhu=make_album('tokyo','jp')
print(zhu)

#print (album_list)
#函数里的字典,调用不能用,也就是不能用返回值以外的
#字典是单次的,对于每个参数是独立的
#返回值的用法忘掉了,重新回忆下