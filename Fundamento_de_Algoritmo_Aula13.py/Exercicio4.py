import string

nome_arquivo = input("Digite o nome do arquivo: ")
contagem = {}

arquivo = open(nome_arquivo, "r")
for linha in arquivo:
    for pontuacao in string.punctuation:
        linha = linha.replace(pontuacao, "")
    
    palavras = linha.lower().split()
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
arquivo.close()

maior_frequencia = max(contagem.values())
palavras_frequentes = [p for p, c in contagem.items() if c == maior_frequencia]

print(f"Frequência máxima: {maior_frequencia} vezes")
print("Palavra(s) mais frequente(s):", palavras_frequentes)
