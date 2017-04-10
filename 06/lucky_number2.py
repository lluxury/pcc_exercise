favorite_number = {
    'bql':['5','8','3'], 
    'txo':['1'], 
    'qtj':['6','2','99']
}

for name , citys in favorite_number.items():
    print("\n" + name.title() + "'s favorite city are:")
    for city in citys:
        print('\t' + city)

#注意循环嵌套的写法,表头,单元...