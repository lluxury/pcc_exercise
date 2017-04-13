def city_country(name, country='China'):
    '''What do I Lent in this chapter?'''
    #print('name is  ' + name +', country is ' + country)
    cc = name.title() + ',' +country.title()
    return cc

care=city_country('sh')
print(care)

xiaoxin = city_country('bj')
print(xiaoxin)

zhu=city_country('tokyo','jp')
print(zhu)

#返回值的用法忘掉了,重新回忆下