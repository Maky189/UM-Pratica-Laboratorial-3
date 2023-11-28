def explode(inteiro):
    if isinstance(inteiro, int):
        tuplo = tuple(elemento for elemento in str(inteiro))
        print(tuplo)
    else:
        raise ValueError("explode: argumento nao inteiro")
explode(34500)