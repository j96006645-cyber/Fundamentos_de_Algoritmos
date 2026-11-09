matriz = []
soma_diagonal = 0

print("Digite os 9 números da matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
        if i == j:
            soma_diagonal += valor
    matriz.append(linha)

print("\nMatriz Digitada:")
for linha in matriz:
    print(linha)

print(f"\nA soma dos elementos da diagonal principal é: {soma_diagonal}")
