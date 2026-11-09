palavras = []
while True:
    palavra = input("Digite uma palavra: ")
    if palavra == "":
        break
    if palavra not in palavras:
        palavras.append(palavra)

print("Palavras digitadas:")
for p in palavras:
    print(p)
