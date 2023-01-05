# HW_2_5**
# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
# random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.
# random.randrange(start, stop, step) возвращает случайно выбранное число из последовательности.

from random import randrange   

def set_array_shuffle_numbers():
    n_len = int(input('Enter the value of list length, please: '))

    lst_1 = list(range(n_len))
    print('Initial list before shuffle:', lst_1)
    
    for i in range(len(lst_1) // 2):
        i_ran = randrange(len(lst_1))
        temp_i = lst_1[i]
        lst_1[i] = lst_1[i_ran]
        lst_1[i_ran] = temp_i
    return lst_1
   
print('Initial list after shaffle: ',set_array_shuffle_numbers())  