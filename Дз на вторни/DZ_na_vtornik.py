otvet = []
poisk = []
shodstwa = []
n = int(input('Введите кол-во строк:'))
for i in range(n):
    num = input('введите строки:')
    otvet.append(n)

k = int(input('введите кол-во поисковых запросов:'))
for i in range(n):
    k1 = input('введите сами  строки:')
    poisk.append(k1)

for i in otvet:
    n = 0
    for j in poisk:
        if j.lower() in i.lower():
            n += 1
        if n >= len(poisk):
            print(i)









