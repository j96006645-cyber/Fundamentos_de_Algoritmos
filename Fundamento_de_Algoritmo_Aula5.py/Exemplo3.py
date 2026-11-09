ultimo = int(input("Digite o ultimo digito da contagem: \n"))
x = 0
while x <= ultimo:
    if x % 2 == 0:
        print(x)
    x = x + 1