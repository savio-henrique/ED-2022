def sort_text(lista):
    ordem = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final = []
    for i in ordem:
        if i in lista:
            for letra in lista:
                if letra in i:
                    final.append(letra)
    return final

def dicio_transform(lista):
    dicio={}
    for letra in lista:
        if letra not in dicio:
            dicio[letra] = 1
        else:
            dicio[letra] += 1
    return dicio

def busca(lista, valor_buscado):
    if isinstance(lista,str):
        lista = dicio_transform(lista)
    for i in valor_buscado:
        if i not in lista:
            return None
        else:
            lista[i] -= 1
            if lista[i] == 0:
                lista.pop(i)

    return lista

def main():
    qtd_testes = int(input())
    for x in range(qtd_testes):
        plano = input()
        for i in range(3):
            buscado = input()
            if plano is not None:
                plano = busca(plano,buscado)
        if plano is not None and len(plano) == 0:
            print("It's in the box!")
        elif plano is not None:
            print("Bora ralar:", end=" ")
            plano = sort_text(plano)
            for l in plano:
                print(l, end="")
            print()
        else:
            print("You died!")

main()