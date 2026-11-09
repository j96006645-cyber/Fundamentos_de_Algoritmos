def data_magica(dia, mes, ano):
    ano_dois_digitos = ano % 100
    return dia * mes == ano_dois_digitos

for ano in range(1901, 2001):
    for mes in range(1, 13):
        for dia in range(1, 32):
            # Verifica se a data é válida
            try:
                from datetime import date
                date(ano, mes, dia)
            except ValueError:
                continue
            
            if data_magica(dia, mes, ano):
                print(f"Data mágica: {dia}/{mes}/{ano}")
