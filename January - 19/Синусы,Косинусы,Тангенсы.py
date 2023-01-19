from math import sin,cos,tan,pow,radians
x = float(input("Введите значение X: "))
x = radians(x)
x = sin(x) + cos(x) + pow(tan(x), 2)
print (x)


