from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("Algoritmos")
janela.geometry('400x400')

def show():
    res = messagebox.askyesno('Sim ou Nao', 'Python e legal?')
    print(res)

botao = Button(janela, text="Perguntar", command=show)
botao.place(x=200, y=200, anchor=CENTER)

janela.mainloop()
