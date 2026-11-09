from random import randint

def lancar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1 + dado2

frequencias = {}

for _ in range(1000):
    soma = lancar_dados()
    if soma in frequencias:
        frequencias[soma] += 1
    else:
        frequencias[soma] = 1

print("Lancamentos:")
print(frequencias)
print()

print("Em 1000 lancamentos tivemos as seguintes porcentagens:")
for soma in sorted(frequencias.keys()):
    porcentagem = (frequencias[soma] / 1000) * 100
    print(f"{soma} : {porcentagem:.1f}%")
