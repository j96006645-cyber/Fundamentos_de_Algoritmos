x = int(input("Digite o tamanho do tabuleiro: "))

for i in range(x):
    for j in range(x):
        if (i + j) % 2 == 0:
            print("0", end="")
        else:
            print("*", end="")
    print()
