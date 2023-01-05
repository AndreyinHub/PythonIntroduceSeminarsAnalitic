# HW_2_4
# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5                       # Enter the value of N: 4
# Position one: 1                               # Position one: 20
# Position two: 2                               # Position two: 22
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]     # -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> 20                                         # -> There are no values for these indexes!
        
n_val = int(input('Enter the value of N, please: '))
print()

lst_1 = []

for i in range(2 * n_val + 1):
    lst_1.append(- n_val + i)
    
print('Result list: ', lst_1)
print()

pos_1 = int(input('Enter position one, please: ')) # Enter position the 1 element, not index:
pos_2 = int(input('Enter position two, please: ')) # Enter position the 2 element, not index:

if pos_1 in range(2 * n_val + 1) and pos_2 in range(2 * n_val + 1):
    print('Product position\'s values:', lst_1[pos_1 - 1] * lst_1[pos_2 - 1])
    print()
    
else:
    print()
    print('There are no values for these indexes!')
    print()