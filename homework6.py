my_dict = {'Bell': 2001, 'Nio': 1997, 'Sus': 2004, 'Pam': 1980}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Nio'))
print('Not existing value:', my_dict.get('Abs'))
my_dict.update({'Ann': 1994, 'Max': 1999})
c = my_dict.pop('Pam')
print('Deleted value:',c)
print('Modified dictionary:', my_dict)

my_set = {1, 2, 3, 3, 3, 'Pam', 'Pam', False, False}
print('Set:', my_set)
my_set.add(8)
my_set.add('Wow')
my_set.discard(1)
print('Modified set:', my_set)



