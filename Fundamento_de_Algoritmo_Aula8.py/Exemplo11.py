z = ['a', 'b', 'c', 'd', 'e']

try:
    posicao = z.index('c')
    print(f"Elemento encontrado no índice {posicao}")
except ValueError:
    print("Elemento não encontrado!")
