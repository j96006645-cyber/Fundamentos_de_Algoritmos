from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("Aulas 13 - Slide 30")
janela.geometry('400x350')

def testar_question():
    res = messagebox.askquestion('Aviso', 'Botao askquestion clicado!')
    print("askquestion retornou:", res)

def testar_yesnocancel():
    res = messagebox.askyesnocancel('Aviso', 'Botao askyesnocancel clicado!')
    print("askyesnocancel retornou:", res)

def testar_okcancel():
    res = messagebox.askokcancel('Aviso', 'Botao askokcancel clicado!')
    print("askokcancel retornou:", res)

def testar_retrycancel():
    res = messagebox.askretrycancel('Aviso', 'Botao askretrycancel clicado!')
    print("askretrycancel retornou:", res)

btn1 = Button(janela, text="Testar askquestion", command=testar_question)
btn1.place(x=200, y=50, anchor=CENTER)

btn2 = Button(janela, text="Testar askyesnocancel", command=testar_yesnocancel)
btn2.place(x=200, y=120, anchor=CENTER)

btn3 = Button(janela, text="Testar askokcancel", command=testar_okcancel)
btn3.place(x=200, y=190, anchor=CENTER)

btn4 = Button(janela, text="Testar askretrycancel", command=testar_retrycancel)
btn4.place(x=200, y=260, anchor=CENTER)

janela.mainloop()
