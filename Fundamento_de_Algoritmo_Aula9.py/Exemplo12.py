quadrados = []
for x in range(10):
    quadrados.append(x * x)


quadrados_comprehension = [x * x for x in range(10)]

print(quadrados)

print(quadrados_comprehension)
