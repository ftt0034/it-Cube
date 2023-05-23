m = int(input('Введите вашу массу:'))
rost = float(input('Введите ваш рост(1):'))
rost1 = float(input('Введите ваш рост(2):'))
IMT = m // (rost * rost1)
if 18.5 <= IMT <= 25:
    print('Оптимальная масса')
if IMT < 18.5:
    print('Недостаточная  масса')
if  IMT > 25:
    print('Избыточная масса')
