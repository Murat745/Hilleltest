a = input('Введите трехзначное число: ', )
b = int(a)

c = b % 10
b = b // 10
d = b % 10
b = b // 10

print('Сумма цифр введенного Вами числа равна: ', b + c + d)