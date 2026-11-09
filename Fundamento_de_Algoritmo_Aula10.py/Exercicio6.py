from random import randint

opcao = input("Digite 'S' para Soma ou 'M' para Média: ").strip().upper()
m = [[randint(0, 9) for _ in range(12)] for _ in range(12)]

soma = 0
quantidade = 0

for i in range(12):
    for j in range(12):
        if i > j:
            soma += m[i][j]
            quantidade += 1

if opcao == 'S':
    print(f"\nSoma dos elementos abaixo da diagonal: {soma}")
elif opcao == 'M':
    media = soma / quantidade
    print(f"\nMédia dos elementos abaixo da diagonal: {media:.2f}")
else:
    print("\nOpção inválida! Escolha apenas S ou M.")
