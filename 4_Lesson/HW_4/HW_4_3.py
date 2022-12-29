# HW_4_3    # 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности 
# в том же порядке.
# посмотреть модуль collection
# in                          in                                          in
# 7                           -1                                          10

# out                         out                                         out
# [4, 5, 3, 3, 4, 1, 2]       Negative value of the amount of numbers!    [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [5, 1, 2]                   []                                          [6, 2, 3, 0, 9]

def non_repeat_lst(lst):
    lst_res = []
    input_lst = input(' Enter num\'s sequence, please: ')
    for i in input_lst:
        if input_lst.count(i) == 1:
            lst_res += [i]
    print(input_lst)
    print('Non repeat numbers: ', lst_res)
    
non_repeat_lst([])