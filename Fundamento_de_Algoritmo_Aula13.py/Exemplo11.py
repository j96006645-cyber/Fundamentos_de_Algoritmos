from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("Algoritmos")
janela.geometry('400x400')

def show():
    res = messagebox.showinfo('Aviso', 'O boto foi clicado!')
    print(res)

botao2 = Button(janela, text="Boto", command=show)
botao2.place(x=200, y=200, anchor=CENTER)

janela.mainloop()
