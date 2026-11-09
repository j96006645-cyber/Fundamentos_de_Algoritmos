km = float(input("digite a quantidade de quilometros percorridos: "))
dias = int(input("digite a quantidade de dias: "))
total_pagar = (dias * 60.00) + (km * 0.15)
print(f"Total a pagar: {total_pagar:.2f}")