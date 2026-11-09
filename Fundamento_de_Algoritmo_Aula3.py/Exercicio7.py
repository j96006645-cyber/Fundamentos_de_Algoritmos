distancia = float(input("Distancia em km: "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"Preço: R$ {preco:.2f}")
