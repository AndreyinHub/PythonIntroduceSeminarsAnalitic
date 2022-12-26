# * 5**. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
# in                                              in
# 8                                               5
# out                                             out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21       5 -3 2 -1 1 0 1 1 2 3 5
# ________________________________________        # ________________________________________

# # _______________START_3.5_________________________

def fibn_1(n):    

    if n in [1,2]:
        return 1
    else:
        return fibn_1(n - 1) + fibn_1(n - 2)
        
fibn_digs = [0]

for j in range(1, 8 + 1):
    fibn_digs.append(fibn_1(j))
    if j % 2 != 0:
        fibn_digs.insert(0, fibn_1(j))
    else:
        fibn_digs.insert(0, -fibn_1(j))
print('Fibonacci numbers: ', *fibn_digs)

# _______________RESULT_3.5_________________________