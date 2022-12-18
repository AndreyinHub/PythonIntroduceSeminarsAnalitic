# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

print()
num = int(input('Input week\'s day number, please: '))
print()
if 0 < num < 6:
    print('Workday')
elif num == 6 or num == 7:
    print('Weekend')
else:
    print('Are you shure? It\'s not a day of the week!')
print()