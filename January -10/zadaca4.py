#задача номер 4 Римские цифры
cifra = int(input("Введите число:"))
if 1 <= cifra <= 10:
    if cifra == 1:
        print("Этой цифре соотвестует - 'I' ")
    elif cifra == 2:
        print("Этой цифре соотвестует - 'II'")
    elif cifra == 3:
        print("Этой цифре соотвестует - 'III'")
    elif cifra == 4:
        print("Этой цифре соотвестует - 'IV'")
    elif cifra == 5:
        print("Этой цифре соотвестует - 'V'")
    elif cifra == 6:
        print("Этой цифре соотвестует - 'VI'")
    elif cifra == 7:
        print("Этой цифре соотвестует - 'VII'")
    elif cifra == 8:
        print("Этой цифре соотвестует - 'VIII'")
    elif cifra == 9:
        print("Этой цифре соотвестует - 'IX'")
    elif cifra == 10:
        print("Этой цифре соотвестует - 'X'")
else:
    print("Ошибка")

