numeros = []
for i in range(10):
    valor = float(input(f"Digite o {i+1} número: "))
    numeros.append(valor)

maior_valor = max(numeros)
indice_maior = numeros.index(maior_valor)

print("Números:", numeros)
print("Maior número:", maior_valor)
print("Índice do maior número:", indice_maior)
