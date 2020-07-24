from tkinter.filedialog import *
from tkinter import *
file = str
dic = {}
mas = []


def my_write(els):
    win = Tk()
    win.withdraw()
    file_name = asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                             ("Chemical elements files", "*.els;*.el"),
                                             ("All files", "*.*")))
    f = open(file_name, 'w', encoding='UTF8')
    els = str(els)
    f.write(els)
    f.close()


def my_read():
    win = Tk()
    win.withdraw()
    global file
    file_name = askopenfilename()
    f = open(file_name, 'r', encoding='UTF8')
    file = f.read()
    f.close()


def my_dict(line):
    global dic
    Any = line.split(';')
    dic = {'el': Any[1], 'name': Any[2], 'num': int(Any[0]), 'mass': float(Any[3]), 'masr': int(Any[4])}

my_read()
for i in file.split('\n'):
    my_dict(i)
    mas.append(dic)
print(mas)

