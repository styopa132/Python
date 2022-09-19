import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN
print('Введите действие')
print('Сложение, вычитание, умножение, деление, возведение в степень, логарифм, округление в большую сторону до N знака после запятой, округление в меньшую сторону до N знака после запятой.')
a = input()
def plus():
        print('Введите первое число')
        q = input()
        while True:
            try:
                float(q)
                q = int(q)
                break
            except ValueError:
                print('Введенный элемент не является числом, введите первый элемент')
                q = input()
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
    q = input()
    while True:
        try:
            float(q)
            q = int(q)
            break
        except ValueError:
            print('Введенный элемент не является числом, введите первый элемент')
            q = input()
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
    q = input()
    while True:
        try:
            float(q)
            q = int(q)
            break
        except ValueError:
            print('Введенный элемент не является числом, введите первый элемент')
            q = input()
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
    q = input()
    while True:
        try:
            float(q)
            q = int(q)
            break
        except ValueError:
            print('Введенный элемент не является числом, введите первый элемент')
            q = input()
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
    while True:
        try:
            w = int(w)
            print(q/w)
            break
        except ZeroDivisionError:
            print('Деление на ноль невозможно, введите второй элемент')
            w = input()
def step():
    print('Введите первое число')
    q = input()
    while True:
        try:
            float(q)
            q = int(q)
            break
        except ValueError:
            print('Введенный элемент не является числом, введите первый элемент')
            q = input()
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
    while True:
        while True:
            print('Введите основание логарифма')
            n = input()
            try:
                float(n)
                n = int(n)
                break
            except ValueError:
                print('Введенный элемент не является числом, введите основание логарифма')
                n = input()
        if n == 0:
            print('Основание логарифма не может быть равно 0')
        elif n == 1:
            print('Основание логарифма не может быть равно 1')
        elif n < 0:
            print('Основание логарифма не может быть отрицательным числом')
        else:
            break
    while True:
        print('Введите аргумент логарифма')
        m = input()
        while True:
            try:
                float(m)
                m = int(m)
                break
            except ValueError:
                print('Введенный элемент не является числом, введите аргумент логарифма')
                m = input()
        if m == 0:
            print('Аргумент логарифма не может быть равен 0')
        elif m == 1:
            print('Аргумент логарифма не может быть равен 1')
        elif m < 0:
            print('Аргумент логарифма не может быть отрицательным числом')
        else:
            break
    print(math.log(m, n))
def bol():
    print('Введите число')
    n = input()
    while True:
        try:
            float(n)
            n = float(n)
            break
        except ValueError:
            print('Введенный элемент не является числом, введите число')
            n = input()
    print('До какого знака необходимо округлить?')
    m = input()
    while True:
        try:
            float(m)
            m = int(m)
            break
        except ValueError:
            print('Введенный элемент не является числом, введите число')
            m = input()
    b = '1.' + '0' * m
    number = Decimal(n)
    print(number.quantize(Decimal(b), ROUND_HALF_UP))
def mal():
    print('Введите число')
    n = input()
    while True:
        try:
            float(n)
            n = float(n)
            break
        except ValueError:
            print('Введенный элемент не является числом, введите число')
            n = input()
    print('До какого знака необходимо округлить?')
    m = input()
    while True:
        try:
            float(m)
            m = int(m)
            break
        except ValueError:
            print('Введенный элемент не является числом, введите число')
            m = input()
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

