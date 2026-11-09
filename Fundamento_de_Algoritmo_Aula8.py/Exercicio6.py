numeros = []

for i in range(10):
    valor = int(input("Digite um numero: "))
    numeros.append(valor)

print("Numeros:", numeros)

for i in range(2, len(numeros)):
    if numeros[i] > numeros[i-1] + numeros[i-2]:
        print(numeros[i])
