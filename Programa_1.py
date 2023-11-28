def filtra_pares(tuplo):
    
    novo_tuplo = tuple(elemento for elemento in tuplo if int(elemento) in range(2, 10, 2))
    return novo_tuplo if novo_tuplo != () else ValueError("Erro no tuplo")

tuplo = ()

for i in range(1, 9):
    tuplo = tuplo + tuple((input(f"elemento numero {i}: ")))
print(filtra_pares(tuplo))