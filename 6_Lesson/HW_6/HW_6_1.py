# HW_6_1. Представлен список чисел. 
# Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. 
# Use comprehension.
# in                                  in
# 9                                   10
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]      [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [16, 3, 7, 10]                      [24, 15, 23, 25]


import random

def do_list_random():
    
    length = int(input('Enter a length of your list, please: '))
    lis = [random.randint(5, 40) for i in range(length)]
    
    return lis

def show_elm_great_prev(lst):
    lst = [lst[i] for i in range(1,len(lst)) if lst[i] > lst[i-1]]    

    return lst

inst_lis = do_list_random()
res_lis = show_elm_great_prev(inst_lis)
print('Instant list:', inst_lis,'\nResult list:', res_lis)