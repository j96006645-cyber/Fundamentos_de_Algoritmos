from tkinter import *

janela = Tk()
janela.title("Algoritmos")
janela.geometry('400x400')

rotulo = Label(janela, text="Hello GUI!", font=("Arial Bold", 14))
rotulo.place(x=200, y=100, anchor=CENTER)

entrada = Entry(janela, width=14, font=("Arial Bold", 14))
entrada.place(x=200, y=50, anchor=CENTER)

def clique():
    resposta = entrada.get()
    rotulo['text'] = resposta

botao = Button(janela, text="Clique aqui!", command=clique)
botao.place(x=200, y=200, anchor=CENTER)

janela.mainloop()
