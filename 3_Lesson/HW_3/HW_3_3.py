# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

# in          in
# 88          11
# out         out
# 1011000     1011
# ________________________________________

def сonvert_dec_num_to_binary():
    
    print('Enter your number, please: ', end= '')
    n_dec = int(input())

    list_bin = []

    while n_dec > 0:
        list_bin.insert(0, n_dec % 2)
        n_dec = n_dec // 2
    return list_bin   

print(*сonvert_dec_num_to_binary(), sep= '')
 # _______________RESULT_3_________________________