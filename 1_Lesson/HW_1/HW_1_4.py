# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*

# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

def quarter_range():
    num = float(input('Input number of quarter: '))    
    if num == 1:
        print('In 1 qurter value\'s x > 0 and y > 0' )
    elif num == 2:
        print('In 2 quarter value\'s x < 0 and y > 0')
    elif num == 3:
        print('In 3 quarter value\'s x < 0 and y < 0')
    elif num == 4:
        print('In 4 quarter value\'s x > 0 and y < 0')
    else:        
        print('The quarter is entered incorrectly. Try again.')
        quarter_range()
quarter_range()
print()