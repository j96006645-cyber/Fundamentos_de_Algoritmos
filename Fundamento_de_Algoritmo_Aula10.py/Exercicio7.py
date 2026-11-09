from random import randint

notas = [[randint(0, 10) for _ in range(3)] for _ in range(10)]

print("--- MATRIZ DE NOTAS (Alunos x Provas) ---")
for i in range(10):
    print(f"Aluno {i}: Prova0={notas[i][0]} | Prova1={notas[i][1]} | Prova2={notas[i][2]}")

print("\n--- RELATÓRIO 1: MENOR NOTA DE CADA ALUNO ---")
for i in range(10):
    menor_nota = min(notas[i])
    idx_prova = notas[i].index(menor_nota)
    print(f"Aluno {i} : menor nota: {menor_nota} , idx: {idx_prova}")

print("\n--- RELATÓRIO 2: MENOR NOTA DE CADA PROVA ---")
for j in range(3):
    notas_da_prova = [notas[i][j] for i in range(10)]
    menor_nota_prova = min(notas_da_prova)
    qtd_alunos = notas_da_prova.count(menor_nota_prova)
    print(f"Menor nota na prova {j} - {menor_nota_prova} (Quantidade de alunos com essa nota: {qtd_alunos})")
