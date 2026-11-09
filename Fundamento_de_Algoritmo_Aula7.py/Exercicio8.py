def data_magica(dia, mes, ano):
    ano_dois_digitos = ano % 100
    if dia * mes == ano_dois_digitos:
        return True
    else:
        return False

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if data_magica(dia, mes, ano):
    print(f"Data mágica: {dia}/{mes}/{ano}")
else:
    print(f"Data comum: {dia}/{mes}/{ano}")
