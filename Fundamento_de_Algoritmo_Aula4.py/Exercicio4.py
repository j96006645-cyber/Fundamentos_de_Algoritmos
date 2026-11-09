nasc = int(input("Ano de nascimento: "))
idade = 2026 - nasc  # Considerando o ano letivo atual

print(f"Idade: {idade} anos")

if idade >= 16 and idade < 18:
    print("Pode votar, mas não pode dirigir.")
elif idade >= 18:
    print("Pode votar e pode tirar a CNH.")
else:
    print("Não tem idade para votar e nem para tirar a CNH.")
