#Task 1.1 Проверка, является ли одно число квадрат другого

n = int(input())
m = int(input())

if n == m ** 2 or m == n ** 2:
    print('Yes')
else:
    print('No')