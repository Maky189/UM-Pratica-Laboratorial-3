def explode(inteiro):
    if isinstance(inteiro, int):
        tuplo = tuple(elemento for elemento in str(inteiro))
        print(tuplo)
    else:
        print(f" {inteiro} nao inteiro")

explode(34500)