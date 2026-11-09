lista = [3, 7, 9, 12, 15]
elemento = int(input("Digite o número que deseja procurar: "))

encontrado = False
for item in lista:
    if item == elemento:
        encontrado = True
        break

if encontrado:
    print(f"O número {elemento} está na lista.")
else:
    print(f"O número {elemento} não está na lista.")
