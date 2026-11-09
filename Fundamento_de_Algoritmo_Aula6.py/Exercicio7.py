num = int(input("Digite um número: "))

a = 0
b = 1
pertence = False

if num == 0 or num == 1:
    pertence = True

while b < num:
    proximo = a + b
    a = b
    b = proximo
    if b == num:
        pertence = True

if pertence:
    print("Verdadeiro")
else:
    print("Falso")
