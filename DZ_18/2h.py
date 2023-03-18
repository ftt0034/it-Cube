s = input('Введите свою строку:')
perviah = s.find('h')
vtoriah = s.rfind('h')
strokac2h= s[perviah:vtoriah+1]
s = s.replace(strokac2h,'')
print(s)