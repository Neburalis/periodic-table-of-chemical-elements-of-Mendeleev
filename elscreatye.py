import math
import webbrowser


def rounding(a):
    if (a-a//1) < 0.5:
        return math.floor(a)
    elif (a-a//1) > 0.4:
        return math.ceil(a)


def my_write(els):
    f = open('test1', 'w', encoding='UTF8')
    els = str(els)
    f.write(els)
    f.close()


def my_input(num=False):
    el = input('Введите вещество ')
    name = input('Введите название вещества ')
    if num == False:
        num = int(input('Введите номер вещества '))
    mass = float(input('Введите массу вещества '))
    masr = rounding(mass)
    print('Элемент #{} с названием {} ({}) имеет массу {}'.format(num, name, el, masr))
    dic = {'el':el, 'num':num, 'mass':mass, 'masr':masr}
    print(dic)
    mas.append(dic)
    print('\n')


webbrowser.open('http://www.hemi.nsu.ru/mends.jpg', new=2)
mas = []
for i in range(1, int(input('Введите количество элементов '))+1):
    my_input(i)
print(mas)
my_write(mas)