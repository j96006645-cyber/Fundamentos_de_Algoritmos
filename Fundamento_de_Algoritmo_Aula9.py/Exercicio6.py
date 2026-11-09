def segundo_maior(lista):
    if len(lista) < 2:
        return None
    lista_unica = list(set(lista))
    lista_unica.sort(reverse=True)
    return lista_unica[1] if len(lista_unica) > 1 else None

print(segundo_maior([10, 20, 4, 45, 99]))
