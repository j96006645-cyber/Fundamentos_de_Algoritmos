pares = open("pares.txt", "w")
impares = open("impares.txt", "w")

for numero in range(1000):
    if numero % 2 == 0:
        pares.write("%d\n" % numero)
    else:
        impares.write("%d\n" % numero)

pares.close()
impares.close()
