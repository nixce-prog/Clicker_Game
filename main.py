from tkinter import *
from random import *
import time

root = Tk()
root.title('Кликалка')
root.geometry('300x400')
root.resizable(False, False)
root['bg'] = 'blue'


x = 0


def boostb1():
    global x
    if x >= 50:
        x -= 50
        boostbtn.configure(text='Boost (150)')
        mainbtn.configure(command=gameb1)
        boostbtn.configure(command=boostb2)
        upd_score()
    else:
        print('Нищий ещё')


def boostb2():
    global x
    if x >= 150:
        x -= 150
        boostbtn.configure(text='Boost (250)')
        mainbtn.configure(command=gameb2)
        upd_score()
    else:
        print('Нищий ещё')


def vivodd():
    wind2 = Tk()
    wind2.title('Вывод')
    wind2.geometry('300x400')
    wind2['bg'] = 'blue'

    def vivod():
        LabelText3.configure(text='Недоступно!')

    LabelText2 = Label(wind2,
                       text='Вывод средств на:',
                       font=('Comic Sens MS', 13),
                       bg='blue',
                       fg='white',
                       height=2
                       )
    LabelText2.place(x=12, y=0)

    cbtn = Button(wind2,
                  text='Карточка',
                  font=('Comic Sans MS', 10),
                  command=vivod,
                  bg='blue',
                  fg='white'
                  )
    cbtn.place(x=40, y=100)

    ctbtn = Button(wind2,
                   text='Крипта',
                   font=('Comic Sans MS', 10),
                   command=vivod,
                   bg='blue',
                   fg='white'
                   )
    ctbtn.place(x=200, y=100)

    LabelText3 = Label(wind2,
                       text=' ',
                       font=('Comic Sens MS', 15),
                       bg='blue',
                       fg='red'
                       )
    LabelText3.place(x=100, y=50)

    wind2.mainloop()


def gameb1():
    global x
    x += 2
    print(x)
    upd_score()


def gameb2():
    global x
    x += 5
    print(x)
    upd_score()


def game():
    global x
    x += 1
    print(x)
    upd_score()


def upd_score():
    LabelScore.configure(text=str(x))


LabelText = Label(root,
                  text='Кликер',
                  font=('Comic Sans MS', 15),
                  bg='blue',
                  fg='white'
                  )
LabelText.place(x=120, y=0)

LabelScore = Label(root,
                   text=str(x),
                   font=('Comic Sans MS', 15),
                   bg='blue',
                   fg='white'
                   )
LabelScore.place(x=150, y=70)

mainbtn = Button(root,
                 text='Кликай!',
                 font=('Comic Sans MS', 15),
                 command=game,
                 bg='blue',
                 fg='white',
                 height=2
                 )
mainbtn.place(x=115, y=150)

boostbtn = Button(root,
                  text='Boost! (50)',
                  font=('Comic Sans MS', 10),
                  command=boostb1,
                  bg='blue',
                  fg='white'
                  )
boostbtn.place(x=40, y=40)

btnvivoda = Button(root,
                   text='Вывод',
                   font=('Comic Sans MS', 10),
                   command=vivodd,
                   bg='blue',
                   fg='white'
                   )
btnvivoda.place(x=200, y=40)
root.mainloop()
