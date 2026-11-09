n = int(input("Digite um valor n positivo: "))
S = 0.0
for i in range(1, n + 1):
    S += 1 / i
print(f"Soma S = {S:.4f}")
