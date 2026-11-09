from math import ceil

pi = 3.1415
altura = float(input("Altura: "))
raio = float(input("Raio: "))

area_base = pi * (raio ** 2)
perimetro = 2 * pi * raio
area_lateral = altura * perimetro
area_total = area_base + area_lateral

litros = area_total / 3
latas = ceil(litros / 5)

if latas == 1:
    preco_unitario = 50.00
elif latas == 2:
    preco_unitario = 48.00
elif latas == 3:
    preco_unitario = 46.00
else:
    preco_unitario = 45.00

custo_total = latas * preco_unitario

print(f"Qtde de latas de tinta: {latas}")
print(f"Custo total: R$ {custo_total:.2f}")
