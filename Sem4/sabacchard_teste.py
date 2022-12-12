def sabacchard(cartas, estado=False, retorno=0):
    if len(cartas) <= 1:
        return cartas[0]
    val_esq = cartas[0]
    val_dir = cartas[-1]

    maior_esq = sabacchard(cartas[1:], not estado, val_esq)
    maior_dir = sabacchard(cartas[0:-1], not estado, val_dir)

    if maior_esq >= maior_dir:
        maior = maior_esq
    else:
        maior = maior_dir

    if estado:
        retorno += maior
        return retorno
    elif not estado:
        return maior


lista = [2, 2, 5, 9, 3, 8]
print(sabacchard(lista))
lista = [7,8,3,4,5,10]
print(sabacchard(lista))
lista = [22,11,7,16,7,17,24,4]
print(sabacchard(lista))

