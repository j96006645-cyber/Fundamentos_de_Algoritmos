intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

while True:
    numero = int(input("Digite um número positivo (ou negativo para encerrar): "))
    
    if numero < 0:
        break
    
    if 0 <= numero <= 25:
        intervalo_0_25 += 1
    elif 26 <= numero <= 50:
        intervalo_26_50 += 1
    elif 51 <= numero <= 75:
        intervalo_51_75 += 1
    elif 76 <= numero <= 100:
        intervalo_76_100 += 1

print("Quantidade nos intervalos:")
print("[0-25]:", intervalo_0_25)
print("[26-50]:", intervalo_26_50)
print("[51-75]:", intervalo_51_75)
print("[76-100]:", intervalo_76_100)
