from random import randint

M = [[randint(0, 9) for _ in range(15)] for _ in range(10)]

print("Matriz Completa:")
for linha in M:
    print(" ".join(map(str, linha)))

print("\nPrimeira coluna da matriz:")
for i in range(10):
    print(M[i][0])
