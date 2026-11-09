matriz = []
lista_somas_impares = []

print("Digite os 16 números da matriz 4x4:")
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

for i in range(4):
    soma_linha = 0
    for j in range(4):
        if matriz[i][j] % 2 != 0:
            soma_linha += matriz[i][j]
    lista_somas_impares.append(soma_linha)

print("\nMatriz informada:")
for linha in matriz:
    print(linha)

print("\nLista com a soma dos ímpares de cada linha:", lista_somas_impares)
