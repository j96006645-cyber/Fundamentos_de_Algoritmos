opcoes = {
    1: "Windows Server",
    2: "Unix",
    3: "Linux",
    4: "Netware",
    5: "Mac OS",
    6: "Outro"
}

votos = {opcao: 0 for opcao in opcoes}

while True:
    voto = int(input("Número da opção (0 para encerrar): "))
    if voto == 0:
        break
    elif voto in opcoes:
        votos[voto] += 1

total = sum(votos.values())

print("\nSistema Operacional | Votos | %")
for codigo, nome in opcoes.items():
    qtd = votos[codigo]
    perc = (qtd / total * 100) if total > 0 else 0
    print(f"{nome:<18} | {qtd:<5} | {perc:.0f}%")

print(f"\nTotal de votos: {total}")

if total > 0:
    vencedor = max(votos, key=votos.get)
    perc_vencedor = votos[vencedor] / total * 100
    print(f"\nSistema Operacional mais votado foi o {opcoes[vencedor]}, com {votos[vencedor]} votos, correspondendo a {perc_vencedor:.0f}% dos votos.")
else:
    print("\nNenhum voto registrado.")
