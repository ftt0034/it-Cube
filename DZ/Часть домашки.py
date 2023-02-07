total = 0
total1 = 0
total2 =1
total3 = 0
total4 = 0
counter = 0
n = int(input())



while n !=0:
    last_digt = n %10
    n = n//10
    total += last_digt
    counter += 1
    total2 *= last_digt


total3 = total/counter

print("Сумма числа N =" + str(total), '\n',"Кол-во цифр в числе N =" + str(counter),'\n',"Произведение цифр числа N =" + str(total2),'\n'"Среднее арифметическое числа N=" + str(total3),'\n',"Сумма его первой и последней цифры числа N=" + str(total4))


