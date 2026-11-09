def count_unique_elements(lista):
    return sum(1 for x in lista if lista.count(x) == 1)

print(count_unique_elements([1, 2, 2, 3, 4, 4, 5]))
