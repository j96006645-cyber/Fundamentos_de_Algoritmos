quantidade = 0
somatoria = 0

while True:
    num = float(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    quantidade += 1
    somatoria += num

if quantidade > 0:
    media = somatoria / quantidade
else:
    media = 0

print("Quantidade:", quantidade)
print("Somatória:", somatoria)
print("Média:", media)
