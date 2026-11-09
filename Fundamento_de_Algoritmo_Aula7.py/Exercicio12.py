def divisao(dividendo, divisor):
    quociente = 0
    resto = dividendo
    while resto >= divisor:
        resto -= divisor
        quociente += 1
    return quociente, resto

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

q, r = divisao(dividendo, divisor)
print(f"Quociente: {q}, Resto: {r}")
