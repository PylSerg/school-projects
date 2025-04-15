# place() - метод розміщення віджетів у вікні
# x= - координата по осі X
# y= - координата по осі Y
# relx= - координата по осі X відносно ширини вікна
# rely= - координата по осі Y відносно висоти вікна
# anchor= - прив'язка до вказаної точки (north, south, east, west, center)

from tkinter import Tk, Label
root = Tk()
root.geometry("640x360")

label_1 = Label(root, text="Hello World")
label_2 = Label(root, text="Hello World")
label_3 = Label(root, text="Hello World")

label_1.place(x=10, y=10)
label_2.place(x=100, rely=0.5)
label_3.place(relx=0.5, y=300, anchor="center")

root.mainloop()