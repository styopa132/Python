import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN
print('Введите действие')
print('Сложение, вычитание, умножение, деление, возведение в степень, логарифм, округление в большую сторону до N знака после запятой, округление в меньшую сторону до N знака после запятой.')
a = input()
def plus():
        print('Введите первое число')
        q = int(input())
        print('Введите второе число')
        w = input()
        while True:
            try:
                float(w)
                w = int(w)
                break
            except ValueError:
                print('Введенный элемент не является числом, введите второй элемент')
                w = input()
        print('Ответ =',q+w)
def minus():
    print('Введите первое число')
    q = int(input())
    print('Введите второе число')
    w = input()
    while True:
        try:
            float(w)
            w = int(w)
            break
        except ValueError:
            print('Введенный элемент не является числом, введите второй элемент')
            w = input()
    print('Ответ =', q - w)
def umn():
    print('Введите первое число')
    q = int(input())
    print('Введите второе число')
    w = input()
    while True:
        try:
            float(w)
            w = int(w)
            break
        except ValueError:
            print('Введенный элемент не является числом, введите второй элемент')
            w = input()
    print('Ответ =', q * w)
def del1():
    print('Введите первое число')
    q = int(input())
    print('Введите второе число')
    w = input()
    while True:
        try:
            float(w)
            w = int(w)
            break
        except ValueError:
            print('Введенный элемент не является числом, введите второй элемент')
            w = input()
    print('Ответ =', q / w)
def step():
    print('Введите первое число')
    q = int(input())
    print('Введите второе число')
    w = input()
    while True:
        try:
            float(w)
            w = int(w)
            break
        except ValueError:
            print('Введенный элемент не является числом, введите второй элемент')
            w = input()
    print('Ответ =', q ** w)
def log():
    print("Введите основание логарифма")
    n = int(input())
    print("Введите аргумент логарифма")
    m = int(input())
    print(math.log(m, n))
def bol():
    print('Введите число')
    n = float(input())
    print('До какого знака необходимо округлить?')
    m = int(input())
    b = '1.' + '0' * m
    number = Decimal(n)
    print(number.quantize(Decimal(b), ROUND_HALF_UP))
def mal():
    print('Введите число')
    n = float(input())
    print('До какого знака необходимо округлить?')
    m = int(input())
    b = '1.' + '0' * m
    number = Decimal(n)
    print(number.quantize(Decimal(b), ROUND_DOWN))
if a == 'Сложение':
    plus()
if a == 'вычитание':
    minus()
if a == 'умножение':
    umn()
if a == 'деление':
    del1()
if a == 'возведение в степень':
    step()
if a == 'логарифм':
    log()
if a == 'округление в большую сторону до N знака после запятой':
    bol()
if a == 'округление в меньшую сторону до N знака после запятой':
    mal()

