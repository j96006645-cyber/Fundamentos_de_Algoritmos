preco = float(input("Digite o preço: R$ "))
codigo = int(input("Digite o código de origem: "))

if codigo == 1:
    print(f"Preço: R$ {preco:.2f} | Sul")
elif codigo == 2:
    print(f"Preço: R$ {preco:.2f} | Norte")
elif codigo == 3:
    print(f"Preço: R$ {preco:.2f} | Leste")
elif codigo == 4:
    print(f"Preço: R$ {preco:.2f} | Oeste")
elif codigo == 5 or codigo == 6 or (codigo >= 25 and codigo <= 30):
    print(f"Preço: R$ {preco:.2f} | Nordeste")
elif codigo >= 7 and codigo <= 9:
    print(f"Preço: R$ {preco:.2f} | Sudeste")
elif codigo >= 10 and codigo <= 20:
    print(f"Preço: R$ {preco:.2f} | Centro-Oeste")
else:
    print(f"Preço: R$ {preco:.2f} | Importado")
