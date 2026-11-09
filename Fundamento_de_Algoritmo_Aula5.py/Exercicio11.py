soma_idade = 0
qtd_idade = 0
soma_salario_homens = 0.0
qtd_homens = 0
qtd_mulheres_abaixo_600 = 0

while True:
    idade = int(input("Digite a idade (negativa para encerrar): "))
    if idade < 0:
        break
        
    sexo = input("Digite o sexo (M/F): ").upper()
    salario = float(input("Digite o salário: R$ "))
    
    soma_idade += idade
    qtd_idade += 1
    
    if sexo == "M":
        soma_salario_homens += salario
        qtd_homens += 1
    elif sexo == "F" and salario < 600.00:
        qtd_mulheres_abaixo_600 += 1

media_idade = soma_idade / qtd_idade if qtd_idade > 0 else 0
media_salario_homens = soma_salario_homens / qtd_homens if qtd_homens > 0 else 0

print(f"Média de idade do grupo: {media_idade:.2f}")
print(f"Média de salário dos homens: R$ {media_salario_homens:.2f}")
print("Mulheres com salário abaixo de R$600,00:", qtd_mulheres_abaixo_600)
