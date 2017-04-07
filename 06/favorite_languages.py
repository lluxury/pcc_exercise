favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

list_name = ['jen', 'sarah','xx']

for name in list_name:
    if name in favorite_languages.keys():
        print("thank you " + name)
    else:
        print ("you have a inquier " + name)