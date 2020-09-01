probel = ' '
vetka = '*'

rows = int(input('Введите количество веток елки '))
otstup = rows-1
igolka = 1

for i in range(rows):
    print((probel*otstup) + (vetka*igolka) + (probel*otstup))
    igolka += 2
    otstup -= 1