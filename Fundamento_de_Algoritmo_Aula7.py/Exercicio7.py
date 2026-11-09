def verificar_doacao(sexo, peso):
    if sexo.lower() == "f":
        if peso >= 50:
            return "Apta a doar sangue"
        else:
            return "Não apta a doar sangue (peso mínimo para mulheres é 50kg)"
    elif sexo.lower() == "m":
        if peso >= 60:
            return "Apta a doar sangue"
        else:
            return "Não apta a doar sangue (peso mínimo para homens é 60kg)"
    else:
        return "Sexo inválido (Digite M ou F)"

sexo_usuario = input("Digite o sexo (M para Masculino / F para Feminino): ")
peso_usuario = float(input("Digite o peso em kg: "))

resultado = verificar_doacao(sexo_usuario, peso_usuario)
print(resultado)
