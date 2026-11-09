N = int(input("Digite um número inteiro maior que zero: "))
contagem = 0

while N > 0:
    contagem += 1
    N = N // 10

print(contagem)
