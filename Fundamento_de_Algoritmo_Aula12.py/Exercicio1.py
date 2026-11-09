arquivo_orig = open("pares.txt", "r")
linhas = arquivo_orig.readlines()
arquivo_orig.close()

linhas_invertidas = linhas[::-1]

arquivo_inv = open("invertido.txt", "w")
for linha in linhas_invertidas:
    arquivo_inv.write(linha)
arquivo_inv.close()
