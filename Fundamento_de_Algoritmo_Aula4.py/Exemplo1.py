a = int(input("Lado a: "))
b = int(input("Lado b: "))
c = int(input("Lado c: "))

if (a < b + c) and (b < a + c) and (c < a + b):
    if (a == b) and (b == c):
        print("Triângulo equilátero")
    else:
        if (a == b) or (a == c) or (b == c):
            print("Triângulo isósceles")
        else:
            print("Triângulo escaleno")
else:
    print("Não Triângulo")
