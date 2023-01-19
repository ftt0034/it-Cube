from math import *
a = float(input('Введите значение А:'))
b = float(input('Введите значение B:'))
c = float(input('Введите значение C:'))

if a == 0:
    print("Начинай заново! ")
D = pow(b, 2) - 4*a*b
if D > 0:
    x1 = -b + sqrt(D)/ 2 * a
    x2 = -b - sqrt(D) / 2 * a
    print(min(x1,x2),max(x1,x2))
if D == 0:
    x = -b + sqrt(D)/ 2 * a

    print(x)
if D < 0:
    print("Нет корней")




