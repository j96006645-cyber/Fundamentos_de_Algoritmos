n = int(input("Digite a quantidade de numeros: "))
numeros = []

for i in range(n):
    valor = int(input("Digite um numero: "))
    numeros.append(valor)

print("Numeros:", numeros)
print("Inverso:")
for i in range(len(numeros)-1, -1, -1):
    print(numeros[i])
