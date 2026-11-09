x = int(input("Digite o tamanho da tabela: "))

for i in range(x):
    for j in range(x):
        if j <= i:
            print("$", end="")
        else:
            print("@", end="")
    print()
