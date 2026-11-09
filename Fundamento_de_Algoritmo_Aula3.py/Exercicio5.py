atual = int(input("Ano atual: "))
nasc = int(input("Ano de nascimento: "))
idade = atual - nasc

if idade >= 18:
    print("Você pode tirar CNH.")
