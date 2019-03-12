import math


def is_armstrong(number):
    if isinstance(number, int) is False:
        return False
    powerValue = len(str(number))
    sum = 0
    for i in str(number):
        sum += pow(int(i), powerValue)
    if sum == number:
        return True
    else:
        return False

