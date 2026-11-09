h = float(input("Digite a altura (ex: 1.75): "))
sexo = input("Digite o sexo (M/F): ").upper()

if sexo == "M":
    peso = (72.7 * h) - 58
    print(f"Peso ideal: {peso:.2f} kg")
elif sexo == "F":
    peso = (62.1 * h) - 44.7
    print(f"Peso ideal: {peso:.2f} kg")
