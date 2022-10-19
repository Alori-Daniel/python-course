#learning dictionary
var2 = {'1901172':'Wisdom',
        '1900223':'Glory',
        '1900132':['Precious', 'dami'],
        '1900142':'Tunmise',
        '1900003':'Eunie',
        '1900272':'Tobi'}
#print(var2['1900132'])
#print(var2.get('190000243', "money"))

#Getting all keys in the dictionary
print(var2.keys())

#getting all valuses in the dictionary
print(var2.values())

#getting all the items in the dictionay
print(var2.items())

#updating a dictionary
var2['David'] = 'Wonder'

for i in var2.keys():
        print(f'{i} is a key')

for i in var2.values():
        print(f'{i} is a value')

for i,j in var2.items():
        print(i)