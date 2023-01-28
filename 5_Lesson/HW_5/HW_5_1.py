# Урок 5. HW_5_1
# Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension
# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.

# in                                            # in
# Number of words: 10                           # Number of words: 6

# out                                           # out
# авб абв бав абв вба бав вба абв абв абв       # ваб вба абв ваб бва абв
# авб бав вба бав вба                           # ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

import random

def del_abv_ltr():
    
    num = int(input('\nEnter number of 3 element\'s words, please: '))
    
    if num <= 0:
        print('The data is incorrect. Try again, please!\n')
        exit ()

    li = ('а', 'б', 'в')
    str_res = []

    for i in range(num):
        str_res.append(''.join(random.sample(li, 3)))
    
    print('Instant sequence: ', " ".join(str_res))
    
    str_without = []
    
    for i in range(0, num):
        if str_res[i] != 'абв':
            str_without.append(str_res[i]) 

    print('Result  sequence: ', " ".join(str_without))
    # print(type(str_without))
    return  " ".join(str_without)

del_abv_ltr()