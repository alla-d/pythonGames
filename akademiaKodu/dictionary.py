# list
# index, value
# users = ['Michal', 'Anna', 'Piotr', 5]

# dictionary
# key : value
# dictionary = {'5': 'five', '6': 'six', '1': 'one'}
# print(dictionary['5'])

dictionary = {'cześć': 'hello', 'mama': 'mother', 'tata': 'father',
              'pies': 'dog', 'dziecko': 'child'}
polish_word = input('Write polish word\n')
dictionary['koniec'] = 'end'
if polish_word in dictionary:
    print(dictionary[polish_word])
else:
    print('Do not find word in dictionary')

