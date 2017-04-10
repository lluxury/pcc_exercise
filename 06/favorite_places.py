favorite_places = {
    'bql':['bj','sh'], 
    'txo':['cs','sh'], 
    'qtj':['xx','sh','bj']
}

for name , citys in favorite_places.items():
    print("\n" + name.title() + "'s favorite city are:")
    for city in citys:
        print('\t' + city)

#注意循环嵌套的写法,表头,单元...