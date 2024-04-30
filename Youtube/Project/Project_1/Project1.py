#  PYTHON CLOCK

from tkinter import *
from time import strftime
root = Tk()
root.title('Clock')


def time():
    string = strftime('%H : %M : %S %p')
    lable.config(text=string)
    lable.after(1000, time)


lable = Label(root, font=('arial', 20, 'bold'),
              background='white', foreground='black')
lable.pack(anchor='center')

time()
mainloop()
