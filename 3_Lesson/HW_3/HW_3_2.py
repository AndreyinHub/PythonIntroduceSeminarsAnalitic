# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in                          in 
# 5                           4
# out                         out
# [2, 2, 4, 8, 8]             [2, 5, 8, 10]
# [16, 16, 4]                 [20, 40]
# ________________________________________
# test_list = [1, 2, 3, 9, 4, 5, 6]
# test_list = [2, 2, 4, 8, 8]
# test_list = [2, 5, 8, 10]

test_list = [2, 2, 4, 8, 8]
t = test_list
length = len(t)
print('Initial list is: ', t)
res_list = []

for i in range(0, length // 2):
    res_list.append(t[i] * t[- i - 1])
if length % 2 != 0:
    res_list.append(t[(length // 2)])

print('Result list, contains multiplied pair\'s numbers, is: ', res_list)
print()
# # ______________RESULT_2__________________________