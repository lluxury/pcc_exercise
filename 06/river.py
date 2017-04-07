river = {
'nile': 'egypt', 
'huang': 'china',

'mississippi':'USA'
}

for key, value in river.items():
    print("The " + key + "runs through " + value +".")

for name in (river.keys()):
    print(name)
for country in (river.values()):
    print(country)