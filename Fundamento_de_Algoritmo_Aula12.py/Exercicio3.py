from random import randint

def ler_para_lista():
    arquivo = open("numeros.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    
    num = []
    for linha in linhas:
        num.append(int(linha.strip()))
    return num

def remover_repetidos(lista_num):
    num_unicos = []
    for item in lista_num:
        if item not in num_unicos:
            num_unicos.append(item)
    return num_unicos

def gravar_unicos(lista_unicos):
    arquivo = open("numeros_unicos.txt", "w")
    for item in lista_unicos:
        arquivo.write(f"{item}\n")
    arquivo.close()

arquivo_gerar = open("numeros.txt", "w")
for _ in range(100):
    arquivo_gerar.write(f"{randint(1, 50)}\n")
arquivo_gerar.close()

num = ler_para_lista()
num_unicos = remover_repetidos(num)
gravar_unicos(num_unicos)
