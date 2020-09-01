probel = ' '
vetka = '*'

rows = int(input('Введите количество веток елки '))
spaces = rows-1
igolka = 1

for i in range(rows):
    print((probel*spaces) + (vetka*igolka) + (probel*spaces))
    igolka += 2
    spaces -= 1