# HW_2_3
# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in              out
# 6               [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# sum             14.071

def fun_1_list_and_sum():
    
    n = int(input('Enter your integer number, please: '))
    lst_n = []
    sum_nums = 0
    
    for i in range(1, n+1):
        r_i = (round(float((1 + 1 / i) ** i), 3))
        sum_nums += r_i
        lst_n.append(r_i)
    
    return lst_n, sum_nums
    
lst_n, sum_nums = fun_1_list_and_sum()
print()
print('Result list:', lst_n, ', their sum:', sum_nums)
print()