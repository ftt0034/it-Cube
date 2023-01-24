from math import pow
n = int(input("Введи число:"))
for i in range(n + 1 ):
    print("Квадрат числа "+ str(i) +  " равен " + str(pow(i, 2)))
