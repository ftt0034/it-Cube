from math import pow,sqrt
a = float(input("Введите значение А:"))
b = float(input("Введите значение B:"))
sra = a + b / 2
srg = sqrt(a*b)
srgg = 2 * a * b / a + b
srk1 = pow(a, 2) + pow(b, 2)
srk = sqrt(srk1/2)
print("С.А.Ч = " + str(sra),"\n,C.Г.Ч = " + str(srg),"\n,С.Г.Ч(1) = " + str(srgg),"\n,C.К.Ч = " + str(srk)  )
