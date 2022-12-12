def sabacchard(cartas, memo={}, estado=False, retorno=0):
    num = " ".join(list(map(str, cartas)))
    if num in memo:
        return memo[num] if not estado else memo[num] + retorno
    if len(cartas) <= 1:
        return cartas[0]
    val_esq = cartas[0]
    val_dir = cartas[-1]

    maior_esq = sabacchard(cartas[1:], memo, not estado, val_esq)
    maior_dir = sabacchard(cartas[0:-1], memo, not estado, val_dir)

    if maior_esq >= maior_dir:
        maior = maior_esq
    else:
        maior = maior_dir

    memo[num] = maior
    if estado:
        retorno += memo[num]
        return retorno
    elif not estado:
        return memo[num]


joga_fora = input()
numeros = list(map(int, input().split()))
print(sabacchard(numeros))

# lista = [2, 2, 5, 9]
# print(sabacchard(lista))
# lista = [7,8,3,4,5,10]
# print(sabacchard(lista))
# lista = [22,11,7,16,7,17,24,4]
# numeros = list(map(int,input().split()))
# print(sabacchard(numeros))

