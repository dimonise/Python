start = int(input('Введите первое число '))
finish = int(input('Введите второе число '))

summ = 0

while start <= finish:
    if start % 2 == 1:
        summ += start

    start+=1

print(summ);