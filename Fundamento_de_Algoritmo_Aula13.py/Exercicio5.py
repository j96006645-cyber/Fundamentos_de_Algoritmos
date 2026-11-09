import string

texto = input("Digite uma linha de texto: ")
pontuacoes = string.punctuation
palavras = texto.split()
resultado = []

for item in palavras:
    sinal = ""
    if item[-1] in pontuacoes:
        sinal = item[-1]
        item = item[:-1]
        
    eh_maiuscula = item.istitle()
    palavra = item.lower()
    
    if palavra[0] in "aeiou":
        nova_palavra = palavra + "way"
    else:
        idx_vogal = 0
        while idx_vogal < len(palavra) and palavra[idx_vogal] not in "aeiou":
            idx_vogal += 1
        nova_palavra = palavra[idx_vogal:] + palavra[:idx_vogal] + "ay"
        
    if eh_maiuscula:
        nova_palavra = nova_palavra.capitalize()
        
    resultado.append(nova_palavra + sinal)

print("Resultado em Pig Latin:", " ".join(resultado))
