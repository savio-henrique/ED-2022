lista = [0,1,1]
def fib(num,lista):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    for x in range(3,num+1):
        lista.append(lista[x-1] + lista[x-2])

    return lista[num]
numero=int(input())
print(f"fibonacci({numero}) = {fib(numero,lista)}")
