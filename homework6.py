my_dict = {'Руслан': 2010, 'Надя': 2009, 'Влад': 2011}
print(my_dict)
print('Existing value: ', my_dict['Надя'])
print('Not existing value: ', my_dict.get('Юля'))
my_dict.update({'Никита': 2008,
                'Полина': 2009})
deleted_value = my_dict.pop('Руслан')
print('Deleted value: ', deleted_value)
print('Modified dictionary: ', my_dict)
from random import randint
my_set = {randint(-10, 10) for i in range(20)}
print(my_set)
my_set.update({randint(30, 40) for i in range(2)})
my_set.discard(3)
print('Modified set:', my_set)