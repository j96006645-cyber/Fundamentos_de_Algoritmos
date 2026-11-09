def procuraChave(dicionario, valor_procurado):
    chaves_encontradas = []
    for chave, valor in dicionario.items():
        if valor == valor_procurado:
            chaves_encontradas.append(chave)
    return chaves_encontradas

meu_dicionario = {
    'alpha': 1,
    'bravo': 2,
    'charlie': 1,
    'delta': 3,
    'echo': 1
}

print("Dicionario:")
print(meu_dicionario)
print()

print("Procurando chaves com valor 1")
resultado_varias = procuraChave(meu_dicionario, 1)
print(resultado_varias)
print()

print("Procurando chaves com valor 3")
resultado_uma = procuraChave(meu_dicionario, 3)
print(resultado_uma)
print()

print("Procurando chaves com valor 4")
resultado_nenhuma = procuraChave(meu_dicionario, 4)
print(resultado_nenhuma)
