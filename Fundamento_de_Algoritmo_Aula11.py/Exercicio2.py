from random import randint

contagem = {}

for _ in range(100):
    numero = randint(0, 20)
    if numero in contagem:
        contagem[numero] += 1
    else:
        contagem[numero] = 1

print("Numero: Quantidade")
for numero in sorted(contagem.keys()):
    print(f"{numero} : {contagem[numero]}")
