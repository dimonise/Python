hrn = int(input('Введите количество гривен '))
kop = int(input('Введите количество копеек '))

if kop >= 100:
    hrn += kop/100
    kop = 0

print(hrn,' гривен',kop,' копеек')