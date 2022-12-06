def ehPossivelPalindromo(palavra=input()):
    contrario = palavra[::-1]
    letras = list(zip(palavra, contrario))
    contador = 0
    for i in letras:
        if i[0] != i[1]:
            contador += 1
    if str(contador) in "02":
        if (len(palavra) % 2 != 0):
            print("POSSÍVEL")
        else:
            if contador != 0:
                print("POSSÍVEL")
            else:
                print("IMPOSSÍVEL")
    else:
        print("IMPOSSÍVEL")
    return

ehPossivelPalindromo()