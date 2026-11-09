numeros = []

for i in range(10):
    valor = int(input(f"Digite o {i+1} número: "))
    numeros.append(valor)

soma_pares = 0
soma_indice_par = 0

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        soma_pares += numeros[i]
    if i % 2 == 0:
        soma_indice_par += numeros[i]

print("Números:", numeros)
print("Soma elementos pares:", soma_pares)
print("Soma elementos índice par:", soma_indice_par)
