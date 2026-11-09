from random import randint

def somar_arquivo():
    arquivo_leitura = open("numeros.txt", "r")
    conteudo = arquivo_leitura.read()
    arquivo_leitura.close()
    
    lista_texto = conteudo.split()
    soma = 0
    for item in lista_texto:
        soma += int(item)
    return soma

arquivo_escrita = open("numeros.txt", "w")
lista_aleatorios = [str(randint(1, 100)) for _ in range(100)]
arquivo_escrita.write(" ".join(lista_aleatorios))
arquivo_escrita.close()

resultado_soma = somar_arquivo()
print(f"Somatória: {resultado_soma}")
