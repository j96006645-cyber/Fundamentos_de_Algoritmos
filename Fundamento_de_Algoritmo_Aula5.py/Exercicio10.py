aprovados = 0
soma_notas = 0.0

for i in range(80):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    soma_notas += nota
    if nota >= 6.0:
        aprovados += 1

media_turma = soma_notas / 80
print("Quantidade de aprovados:", aprovados)
print(f"Média da turma: {media_turma:.2f}")
