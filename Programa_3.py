def junta_ordenados(tuplo1, tuplo2):
    for elemento in tuplo2:
        tuplo1 = tuplo1 + (elemento, )
    return sorted(tuplo1)  

print(junta_ordenados((2, 34, 200, 210), (1, 23)))