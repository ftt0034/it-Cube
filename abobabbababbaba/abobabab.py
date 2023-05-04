
def find_all(target, symbol):
    serch = []
    while symbol in target:
        x = target.find(symbol)

        serch.append(x)
        target = target[:x] + target[x + 1:]
    return target









