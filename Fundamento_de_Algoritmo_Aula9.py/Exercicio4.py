palavra = "EVAPARAR"
letras_descobertas = ["_"] * len(palavra)
tentadas = set()

while "_" in letras_descobertas:
    print(" ".join(letras_descobertas))
    letra = input("Digite uma letra: ").upper()

    if letra in tentadas:
        print("Você já tentou essa letra!")
        continue

    tentadas.add(letra)

    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                letras_descobertas[i] = letra
        print("Boa!")
    else:
        print("Incorreta!")

print("Parabéns! Você descobriu a palavra:", palavra)
