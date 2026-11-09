def exponencial(n):
    for b in range(2, n+1):
        k = 1
        valor = b
        while valor < n:
            valor *= b
            k += 1
        if valor == n:
            return b, k
    return None, None

n = int(input("Digite um número: "))
b, k = exponencial(n)

if b is not None:
    print(f"{b}^{k} = {n}")
else:
    print("Não foi possível encontrar b e k.")
