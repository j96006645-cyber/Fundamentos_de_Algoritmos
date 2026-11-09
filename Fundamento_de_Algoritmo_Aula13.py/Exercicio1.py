texto = input("Digite uma string: ")
resultado = ""

for caractere in texto:
    if caractere in "aeiou":
        resultado += caractere.upper()
    else:
        resultado += caractere

print("Nova string:", resultado)
