while True:
    num = int(input("Solicite um número entre 0 e 10: "))
    if num >= 0 and num <= 10:
        print("número aceito")
        break
    else:
        print("Erro: valor inválido!")
