hrn = int(input('Введите количество гривен '))
kop = int(input('Введите количество копеек '))
kopString = ''

if kop >= 100:
    hrn += kop / 100
    kop = 0

if kop < 100:
    if kop == 1:
        kopString = ' копейка'
    elif 4 < kop < 21 or 4 < kop % 10 < 10 or kop % 10 == 0:
        kopString = ' копеек'
    elif 1 < kop % 10 < 5:
        kopString = ' копейки'

print(hrn, ' гривен', kop, kopString)
