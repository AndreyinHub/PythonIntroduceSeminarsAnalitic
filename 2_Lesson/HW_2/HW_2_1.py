# HW_2_1.
# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

def sum_digs_real_numb():
    print()
    num = input('Enter your real number, please: ')
    
    # Без round() алгоритм ломается за счет "хвоста" типа 1.2345599999999998e+24
        # при сочетаниях 1234.56, 123.456, 12.3456, 0.123456 Sum = 146, 
        # а при 1.23456 вообще Sum = 176, 
    # "Короткие" округления дают неочевидный результат типа:
        # round(num, 2): Enter your real number, please: 1.23456 => Sum =  6 (1+2+3)
    # Получилось только с "костылем":
        # lngth = len(num) => num = float(num) => num = round(num, lngth - 1) * 10    
        
    lngth = len(num)
    num = float(num)

    while num % 10 > 0:
        num = round(num, lngth - 1) * 10
   
    num_r = int(num)
    sum_dig = 0

    while num_r > 0:

        sum_dig += num_r % 10
        num_r = num_r // 10

    return sum_dig

print('Sum of all digs in number', sum_digs_real_numb())
print()