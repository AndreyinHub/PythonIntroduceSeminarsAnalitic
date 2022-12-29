# 1. Вычислить число c заданной точностью d
# здесь не округление, а именно возможность работы прог с заданной точностью
# in                                                  out
# Enter a real number: 9                              9.000000
# Enter the required accuracy '0.0001': 0.000001

# in                                                  out
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001         8.988
# int_num_part; fract_num_part

from decimal import Decimal

def set_calc_accuracy():
    user_num = input("Enter a real number: ")
    accuracy = input("Enter the required accuracy in form <<0.0001>> : ")

    num = Decimal(user_num)
    num = num.quantize(Decimal(accuracy))
    print(num)
    
    return num

set_calc_accuracy()