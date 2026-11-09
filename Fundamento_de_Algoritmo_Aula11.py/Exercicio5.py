def e_anagrama(str1, str2):
    palavra1 = str1.replace(" ", "").lower()
    palavra2 = str2.replace(" ", "").lower()
    
    if len(palavra1) != len(palavra2):
        return False
        
    contagem1 = {}
    contagem2 = {}
    
    for letra in palavra1:
        contagem1[letra] = contagem1.get(letra, 0) + 1
        
    for letra in palavra2:
        contagem2[letra] = contagem2.get(letra, 0) + 1
        
    return contagem1 == contagem2

p1 = input("Digite uma palavra: ")
p2 = input("Digite outra palavra: ")

if e_anagrama(p1, p2):
    print("São anagramas")
else:
    print("Não são anagramas")
