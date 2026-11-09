maior = 0
for i in range(6):
    num = int(input("Digite um número inteiro positivo: "))
    if num > maior:
        maior = num
print("Maior número lido:", maior)
