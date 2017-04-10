cities = {
    'bj':{
    'country':'cn',
    'population':'100w',
    'event':'qh'
    }
    , 
        'sh':{
    'country':'cn',
    'population':'2200w',
    'event':'dfmz'
    }
    , 
        'ny':{
    'country':'USA',
    'population':'100w',
    'event':'obm'
    }
    
    }

for name, city  in cities.items():
    print("\n" + name + "'s favorite city are:")
    #for cit in city:
    print('\t' + city['country'] +'\t'+ city['population'] +'\t'+ city['event'])

#注意循环嵌套的写法,表头,单元...