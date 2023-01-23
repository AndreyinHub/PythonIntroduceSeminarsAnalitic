# HW_6_2. 
# Для чисел в пределах от 20 до N найти числа, 
#     кратные 20 или 21. Use comprehension.
# in                                      in
# 100                                     424

# out                                     out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]   [20, 21, 40, 42, 60, 63, 80, 84, 100,\ 
#                                         105, 120, 126, 140, 147, 160, 168, 180,\
#                                         189, 200, 210, 220, 231, 240, 252, 260, \
#                                         273, 280, 294, 300, 315, 320, 336, \
#                                         340, 357, 360, 378, 380, 399, 400, 420]

def num_mltypl():
    
    n_max = int(input('Enter natural positive "N"- the max value of your list, please: '))

    lis = [i for i in range(20, n_max + 1) if i % 20 == 0 or i % 21 == 0]
    
    print(lis)
    return lis

num_mltypl()