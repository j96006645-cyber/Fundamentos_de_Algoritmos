from random import randint

A = [[randint(0, 99) for _ in range(5)] for _ in range(10)]

print("Matriz A original (10x5):")
for linha in A:
    print(linha)

At = [[A[i][j] for i in range(10)] for j in range(5)]

print("\nMatriz Transposta At (5x10):")
for linha in At:
    print(linha)
