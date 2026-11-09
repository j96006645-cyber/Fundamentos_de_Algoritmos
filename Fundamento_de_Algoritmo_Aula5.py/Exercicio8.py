somatoria = 0
while True:
    num = float(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    somatoria += num
print("Somatória:", somatoria)
