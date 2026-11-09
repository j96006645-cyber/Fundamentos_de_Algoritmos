dias = int(input("digite a quantidade de dias: "))
horas = int(input("digite a quantidade de horas: "))
minutos = int(input("digite a quantidade de minutos: "))
segundos = int(input("digite a quantidade de segundos: "))
total_segundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos
print(f"tempo total foi de {total_segundos} segundos")