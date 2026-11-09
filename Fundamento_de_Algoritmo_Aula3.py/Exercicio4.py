salario = float(input("Digite o salario: "))

if salario > 1250:
    novo_salario = salario * 1.10
else:
    novo_salario = salario * 1.15

print(f"Novo salario: R$ {novo_salario:.2f}")
