from math import pow, sqrt, sin, cos, tan, log

def dan():
    a = int(input('Введіть число a: '))
    b = int(input('Введіть число b: '))
    return a, b


def one_c():
    a = int(input('Введіть число a: '))
    return a


def add():
    a, b = dan()
    print('a + b = ', a + b)


def minus():
    a, b = dan()
    print('a - b = ', a - b)


def dob():
    a, b = dan()
    print('a * b = ', a * b)


def div():
    a, b = dan()
    if b != 0:
        print(a / b)
    else:
        print('Namojno')


def stepin():
    a, b = dan()
    print('a в степені b = ', pow(a, b))


def qwadr():
    a = one_c()
    print('Квадратний корінь a  = ', sqrt(a))


def qube():
    a = one_c()
    print('Кубічний корінь a  = ', a ** (1 / 3))


def sinus():
    a = one_c()
    print('Синус a  = ', sin(a))


def cosinus():
    a = one_c()
    print('Косинус a  = ', cos(a))


def tangens():
    a = one_c()
    print('Тангенс a  = ', tan(a))

def logarifm():
    a = one_c()
    print('Логарифм a  = ', log(a))


while True:
    print('''\nДія:\n\t+ Доавання\n\t- Віднімання\n\t* Множення\n\t/ Ділення\n\t^ Зведення в ступінь\n\t/2 Квадратний корінь\
    \n\t/3 Кубічний корінь\n\tsin Синус\n\tcos Косинус\n\ttan Тангенс\n\tlog Логарифм\n\t0 Вихід\n''')
    choice = input('Введіть дію: ')
    if choice == '+':
        add()
    elif choice == '-':
        minus()
    elif choice == '*':
        dob()
    elif choice == '/':
        div()
    elif choice == '^':
        stepin()
    elif choice == '/2':
        qwadr()
    elif choice == '/3':
        qube()
    elif choice == 'sin':
        sinus()
    elif choice == 'cos':
        cosinus()
    elif choice == 'tan':
        tangens()
    elif choice == 'log':
        logarifm()
    elif choice == '0':
        print('exit')
        break









