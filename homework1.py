hrn = int(input('Введите количество гривен '))
kop = int(input('Введите количество копеек '))
kopString = ''

if kop >= 100:
    hrn += kop / 100
    kop = 0

if hrn % 10 == 1 and hrn != 11:
    hrnString = ' гривна'
elif 4 < hrn < 21 or 4 < hrn % 10 < 10 or hrn % 10 == 0:
    hrnString = ' гривен'
elif 1 < hrn % 10 < 5:
    hrnString = ' гривны'

if kop < 100:
    if kop % 10 == 1 and kop != 11:
        kopString = ' копейка'
    elif 4 < kop < 21 or 4 < kop % 10 < 10 or kop % 10 == 0:
        kopString = ' копеек'
    elif 1 < kop % 10 < 5:
        kopString = ' копейки'

print(hrn, hrnString, kop, kopString)
