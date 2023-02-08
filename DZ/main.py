total = 0
total1 = 0
total2 =1
total3 = 0

counter = 0
n = int(input())



while n !=0:
    last_digt = n %10
    n = n//10
    total += last_digt
    counter += 1
    total2 *= last_digt

tota= n//10**counter-1 + n%10
total3 = total/counter
tota1 = n//10**counter-1
print("Сумма числа N =" + str(total), '\n',"Кол-во цифр в числе N =" + str(counter),'\n',"Произведение цифр числа N =" + str(total2),'\n'"Среднее арифметическое числа N=" + str(total3),'\n',"Сумма его первой и последней цифры числа N=" + str(tota),'\n',"Первая цифра чилса N - это: "+ str(tota1))
