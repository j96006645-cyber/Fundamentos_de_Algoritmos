def eh_par(num):
    return num % 2 == 0

numeros = [1, 2, 3, 4, 5, 6]
numeros_pares = filter(eh_par, numeros)

print(list(numeros_pares))
