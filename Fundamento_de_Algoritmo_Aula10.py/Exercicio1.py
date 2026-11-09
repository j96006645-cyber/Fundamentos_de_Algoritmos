from random import randint, random

inteiros = [randint(0, 10) for _ in range(10)]
reais = [random() * 10 for _ in range(5)]
strings = ['Python', 'Matriz', 'Lista', 'Algoritmos', 'FEI', 'Computação', 'Dados']

print("Inteiros originais:", inteiros)
print("Reais originais:", reais)
print("Strings originais:", strings)

completa = [inteiros, reais, strings]

del inteiros
del reais
del strings

print("\nLista Completa Aninhada:", completa)
