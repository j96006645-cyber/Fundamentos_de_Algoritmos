from tkinter import *

janela = Tk()
janela.title("Algoritmos")
janela.geometry('400x400')

rotulo = Label(janela, text="Hello GUI!", font=("Arial Bold", 14))
rotulo.place(x=200, y=100, anchor=CENTER)

janela.mainloop()
