ganho_por_hora = float(input("Digite o valor da hora de trabalho: "))
horas_trabalhadas = float(input("Digite o numero de horas trabalhadas no mes: "))
salario_bruto = ganho_por_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato
print(f"\n+ Salario Bruto: R$ {salario_bruto:.2f}")
print(f"- IR (11%): R$ {ir:.2f}")
print(f"- INSS (8%): R$ {inss:.2f}")
print(f"- Sindicato (5%): R$ {sindicato:.2f}")
print(f"= Salario liquido: R$ {salario_liquido:.2f}")