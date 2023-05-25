Timur = input('Что показал Тимур?:').lower()
Ruslan = input('Что показал Руслан?:').lower()
if Timur == 'ножницы' and Ruslan == 'бумага' or Timur == 'камень' and Ruslan == 'ножницы' or Timur == 'бумага' and Ruslan == 'камень':
    print('Победа Тимура!')
elif Ruslan == 'ножницы' and Timur == 'бумага' or Ruslan == 'камень' and Timur == 'ножницы' or Ruslan == 'бумага' and Timur == 'камень':
    print('Победа РУслана!')
elif Timur == 'ножницы' and Ruslan == 'ножницы' or Timur == 'камень' and Ruslan == 'камень' or Timur == 'бумага' and Ruslan == 'бумага':
    print('ничья')