# HW_2_2
# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

# n = int(input('Enter your integer number, please: '))
# lst_m = []
# print(lst_m)
# lst_m.append(1)
# print(lst_m)
# for i in range(n):
#     lst_m.append(int((i + 1) * lst_m[i]))
# lst_m.remove(1)
# print(lst_m)
# # #_______________ HW_2_2 version END____________

def fact_int_num_in_list():
    
    n = int(input('Enter your integer number, please: '))
    lst_fact = [1] * n
        
    for i in range(1, n):
        lst_fact[i] =  (i + 1) * lst_fact[i-1]
    
    return lst_fact

print(fact_int_num_in_list())