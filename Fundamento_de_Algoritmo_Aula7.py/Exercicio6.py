import math

def calcular_formula(n1, n2, n3):
    raiz1 = math.sqrt(n1)
    raiz2 = math.sqrt(n2)
    raiz3 = math.sqrt(n3)
    
    conta1 = (n1 + n2) / 2
    conta2 = (n2 + n3) / 2
    conta3 = (n1 + n3) / 2
    
    resultado = raiz1 + raiz2 + raiz3 + conta1 + conta2 + conta3
    return resultado

print(calcular_formula(4, 9, 16))
