a = int(input("Введите значение А:"))
b = int(input("Введите значение B:"))
a1 = int(input("Введите значение А1:"))
b1 = int(input("Введите значение B1:"))
hod = a - a1
hod1 = b - b1
if hod == 1 and hod1 == 2 or hod == 2 and hod1 == 1:
    print("ДА")
else:
    print('НЕТ')