qtd_testes = int(input("Digite a qtde de números a serem testados: "))
primos = 0

for i in range(qtd_testes):
    num = int(input(f"Digite o número {i+1}: "))
    if num > 1:
        eh_primo = True
        for d in range(2, num):
            if num % d == 0:
                eh_primo = False
                break
        if eh_primo:
            primos += 1

print(f"Você digitou {primos} números primos de um total de {qtd_testes} números")
