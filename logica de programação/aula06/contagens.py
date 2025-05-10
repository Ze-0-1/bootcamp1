def lista():
    lista = list(range(1, 11, ))
    print(lista)


def um_por_um():
    for numero in range(1, 11):
        print(numero)


def com_passo():
    for numero in range(5, 50, 5):
        print(numero)


def regressivo():
    for numero in range(100, 0, -2):
        print(numero)


# lista()
# um_por_um()
# com_passo()
regressivo()
