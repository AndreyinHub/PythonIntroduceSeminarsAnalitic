# * 4*. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
# in                                          in
# 5                                           3
# out                                         out
# [5.16, 8.62, 6.57, 7.92, 9.22]              [9.26, 8.5, 1.14]              
# Min: 0.16, Max: 0.92. Difference: 0.76      Min: 0.14, Max: 0.5. Difference: 0.36                            
# ________________________________________
# # list_float = [9.26, 8.5, 1.14] 
list_float = [5.16, 8.62, 6.57, 7.92, 9.22]

def find_min_max_fract_float_elem(list_int):
    l_f = list_int
    print('Initial list: ', l_f)
    max_elem = round((l_f[0] - int(l_f[0])), 2)
    min_elem = round((l_f[0] - int(l_f[0])), 2)

    for i in range(0, len(l_f)):
        l_f[i] = round((l_f[i] - int(l_f[i])), 2)
        
        if  l_f[i] > max_elem:
            max_elem = l_f[i]
        elif l_f[i] < min_elem:
            min_elem = l_f[i]
    
    print('Result list:  ', l_f)
    print()
    print('Max fractional volume: ', max_elem, 
          'Min fractional volume: ', min_elem, 
          ' and their difference: ', round((max_elem - min_elem), 2))
    # print(' and their difference: ', round((max_elem - min_elem), 2))
    print()

find_min_max_fract_float_elem(list_float)
# _______________RESULT_4_________________________