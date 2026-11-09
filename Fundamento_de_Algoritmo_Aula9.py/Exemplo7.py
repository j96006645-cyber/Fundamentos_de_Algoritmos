temperaturas = [20, 25, 32]
celsius_para_fahrenheit = map(lambda c: (c * 9/5) + 32, temperaturas)

print(list(celsius_para_fahrenheit))
