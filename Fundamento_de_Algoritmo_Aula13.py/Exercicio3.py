import string

nome_arquivo = input("Digite o nome do arquivo: ")
comprimento_maximo = 0
palavras_longas = []

arquivo = open(nome_arquivo, "r")
for linha in arquivo:
    for pontuacao in string.punctuation:
        linha = linha.replace(pontuacao, "")
    
    palavras = linha.split()
    for palavra in list(palavras):
        tamanho = len(palavra)
        if tamanho > comprimento_maximo:
            comprimento_maximo = tamanho
            palavras_longas = [palavra]
        elif tamanho == comprimento_maximo and palavra not in palavras_longas:
            palavras_longas.append(palavra)
arquivo.close()

print(f"Tamanho da palavra mais longa: {comprimento_maximo}")
print("Palavras encontradas:", palavras_longas)
