def ordenar(I, A, B, C):
    if I == 1:
        return sorted([A, B, C])
    elif I == 2:
        return sorted([A, B, C], reverse=True)
    elif I == 3:
        maior = max(A, B, C)
        numeros = [A, B, C]
        numeros.remove(maior)
        return [numeros[0], maior, numeros[1]]

print(ordenar(1, 5, 2, 9))   # ordem crescente
print(ordenar(2, 5, 2, 9))   # ordem decrescente
print(ordenar(3, 5, 2, 9))   # maior no meio
