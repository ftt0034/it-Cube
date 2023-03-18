s = input("Введите свою строку:")
if s.count('f') == 1:
    print('В строке обнаружено одна "f",вот ее индекс ' + str(s.find('f')))
elif s.count('f') == 2:
    print('В строке обнаружено две "f",вот их индексы ' + str(s.find('f')) , str(s.rfind('f')))
else:
    print('NO')
