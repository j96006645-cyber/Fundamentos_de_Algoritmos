from tkinter import *

window = Tk()
window.title("Nova tela")
window.geometry('350x200')

btn1 = Button(window, text="Botao 1")
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)

btn2 = Button(window, text="Botao 2")
btn2.place(x=100, y=50, anchor=CENTER)

window.mainloop()
