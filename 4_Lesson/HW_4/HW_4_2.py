# HW_4_2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# Простые делители числа
# Простые делители числа онлайн

# in              in                      in
# 54              9990                    650
# out             out                     out
# [2, 3, 3, 3]    [2, 3, 3, 3, 5, 37]     [2, 5, 5, 13]

def fact_num_to_simpl_divs():
    num = (int(input('Еnter a number, please: ')))
    lst_divs = []
    samp_divs = 2
    while samp_divs ** 2 <= num:
        if num % samp_divs == 0:
            lst_divs.append(samp_divs)
            num = num // samp_divs
        else:
            samp_divs = samp_divs + 1
    if num > 1:
        lst_divs.append(num)
    return lst_divs
print(fact_num_to_simpl_divs())