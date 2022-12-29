# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in                          in
# 5                           4
# out                         out
# [10, 2, 3, 8, 9]            [4, 2, 4, 9]
# 22                          8
# ________________________________________

def find_sum_odd_position_lists_elem():
    
    import random
    print('Input list\'s length what you want: ', end= '')
    leng_list = int(input())
       
    list_rundom = list(range(0, leng_list ))
   
    sum_elements = 0
    for i in range(leng_list):
        list_rundom[i] = random.randint(1, 20)
        
    for i in range(0,leng_list,2):
        sum_elements += list_rundom[i]
    
    print('We have next list: ', list_rundom)
    return sum_elements
    
print('And its odd position element\'s sum is: ', find_sum_odd_position_lists_elem())
# # ______________RESULT_1__________________________
