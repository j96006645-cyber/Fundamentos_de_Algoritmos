pares = open("pares.txt", "r")
multiplos4 = open("multiplos4.txt", "w")

for linha in pares.readlines():
    numero = int(linha.strip())
    if numero % 4 == 0:
        multiplos4.write("%d\n" % numero)

pares.close()
multiplos4.close()
