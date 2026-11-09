valores = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º valor: "))
    valores.append(numero)

print("Lista completa:", valores)
print("Primeiro elemento:", valores[0])
print("Último elemento:", valores[-1])
