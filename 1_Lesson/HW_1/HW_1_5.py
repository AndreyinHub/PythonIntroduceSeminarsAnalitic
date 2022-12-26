# 5. Напишите программу, которая 
# принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве. 

# - 3
# - 6
# - 2
# - 1
# out 5.099

def distance_points_2D():
    print('Input X and Y coordinates point A')
    x_a = float(input('x: '))
    y_a = float(input('y: '))
    
    print('Input X and Y coordinates point B')
    x_b = float(input('x: '))
    y_b = float(input('y: '))
    length = round((((x_b - x_a)**2 + (y_b - y_a)**2)**0.5), 3)

    print('Distance from A to B is: ', length)
    print()

distance_points_2D()