def contar_caracteres_unicos(texto):
    caracteres = {}
    for letra in texto:
        caracteres[letra] = True
    return len(caracteres)

entrada_usuario = input("Digite uma string: ")
resultado = contar_caracteres_unicos(entrada_usuario)

print(f"Número de caracteres únicos: {resultado}")
