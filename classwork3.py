# # Type range
#
# for i in range(5):
#     print(i,end=', ')
# print()
# for i in range(5,10):
#     print(i,end=', ')
# print()
# for i in range(5,15,2):
#     print(i,end=', ')
# print()
#
# #Перебор используя continue - встречая равенство условия, дальше не идем а возвращаемся на итерацию выше
# for i in 'hello world':
#     if i == 'o':
#         continue
#     print(i,end=' ')
# print()
#
# #Перебор используя break - встречая равенство условия, дальше не идем , стопаем цикл // вся чушь регистрозависимая
# for i in 'hello world':
#     if i == 'w':
#         break
#     print(i,end=' ')
# print()
# #Условный оператор для for - else // капец
# for i in 'hello world':
#     if i == 'а':
#         break
#     print(i, end=' ')
# else:
#     print('No words')


###############################################

ruch = 10
kar = 5
last = 2

for i in range(100//ruch+1):
    for n in range(100//kar+1):
        for v in range(100//last+1):
            if (i+n+v == 30) and (i*ruch + n*kar + v*last == 100):
                print('Ruchki ',i)
                print('Karandashi ',n)
                print('Lastik ',v)
                print()

