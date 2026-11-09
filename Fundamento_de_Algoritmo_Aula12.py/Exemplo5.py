arquivo_escrever = open("contatos.txt", "w")

while True:
    nome = input("Digite o nome: ")
    if nome == "":
        break
    telefone = input("Digite o telefone: ")
    arquivo_escrever.write(f"{nome},{telefone}\n")

arquivo_escrever.close()

arquivo_ler = open("contatos.txt", "r")

for linha in arquivo_ler.readlines():
    print(linha.strip())

arquivo_ler.close()
