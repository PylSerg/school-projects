from tkinter import *

root = Tk()
root.geometry("400x300")

# Створюємо зображення за допомогою PhotoImage()
# PhotoImage(file="img.png").subsample(x, y) - зменшує зображення
# PhotoImage(file="img.png").zoom(x, y) - збільшує зображення
background_image = PhotoImage(file="background_01.png")

background = Label(root, image=background_image)

text = Label(root, text="Hello World!", font="Arial 20 normal")

background.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)
text.place(x=30, y=30)

root.mainloop()