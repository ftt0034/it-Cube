aboba = int(input("Введите значение 1:"))
biba = int(input("Введите значение 2:"))
cok = int(input("Введите значение 3:"))
if aboba == biba and biba == cok:
    print("3")
if aboba != biba and biba == cok or aboba == biba and biba != cok:
    print("2")
if aboba != biba and biba != cok:
    print("0")


