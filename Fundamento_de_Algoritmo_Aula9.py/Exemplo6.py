def quadrado(num):
    return num * num

numeros = [1, 2, 3, 4]
quadrado_numeros = map(quadrado, numeros)

print(list(quadrado_numeros))
