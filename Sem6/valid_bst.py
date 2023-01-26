class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def constituiArvoreBinariaDeBusca(no):
    if no is None:
        return True
    if no.esq is None and no.dir is None:
        return True
    if no.esq is not None:
        if no.esq.dado > no.dado:
            return False
    if no.dir is not None:
        if no.dir.dado < no.dado:
            return False

    return constituiArvoreBinariaDeBusca(no.dir) and constituiArvoreBinariaDeBusca(no.esq)


#Testes
#Teste 1
raiz = ArvoreBinaria(2, ArvoreBinaria(1), ArvoreBinaria(3))
print(constituiArvoreBinariaDeBusca(raiz))
#Teste 2
print()
raiz = ArvoreBinaria(10, ArvoreBinaria(8), ArvoreBinaria(28, ArvoreBinaria(26), ArvoreBinaria(30)))
print(constituiArvoreBinariaDeBusca(raiz))
#Teste 3
print()
raiz = ArvoreBinaria(7, ArvoreBinaria(4), ArvoreBinaria(10, ArvoreBinaria(11), ArvoreBinaria(15)))
print(constituiArvoreBinariaDeBusca(raiz))
#Teste 4
print()
raiz = ArvoreBinaria(0)
print(constituiArvoreBinariaDeBusca(raiz))
#Teste 5
print()
raiz = ArvoreBinaria(2, ArvoreBinaria(1), None)
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(2, ArvoreBinaria(3), None)
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(2, None, ArvoreBinaria(1))
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(2, None, ArvoreBinaria(3))
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(2)
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(2, ArvoreBinaria(0), None)
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(2, None, ArvoreBinaria(0))
print(constituiArvoreBinariaDeBusca(raiz))
#Teste 6
print()
raiz = ArvoreBinaria(19, ArvoreBinaria(31, ArvoreBinaria(3, ArvoreBinaria(7, None, None), ArvoreBinaria(29, None, None)), ArvoreBinaria(10, ArvoreBinaria(5, None, None), ArvoreBinaria(14, None, None))), ArvoreBinaria(9, ArvoreBinaria(15, ArvoreBinaria(18, None, None), ArvoreBinaria(21, None, None)), ArvoreBinaria(28, ArvoreBinaria(8, None, None), ArvoreBinaria(17, None, None))))
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(9, ArvoreBinaria(28, ArvoreBinaria(27, ArvoreBinaria(20, None, None), ArvoreBinaria(6, None, None)), ArvoreBinaria(15, ArvoreBinaria(23, None, None), ArvoreBinaria(13, None, None))), ArvoreBinaria(29, ArvoreBinaria(18, ArvoreBinaria(24,
None, None), ArvoreBinaria(14, None, None)), None))
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(29, ArvoreBinaria(4, None, ArvoreBinaria(18, ArvoreBinaria(11, None, None), ArvoreBinaria(20, None, None))), None)
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(6, None, ArvoreBinaria(31, ArvoreBinaria(22, ArvoreBinaria(8, None, None), None), None))
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(28, ArvoreBinaria(4, ArvoreBinaria(22, ArvoreBinaria(8, None, None), ArvoreBinaria(16, None, None)), ArvoreBinaria(18, ArvoreBinaria(0, None, None), ArvoreBinaria(20, None, None))), ArvoreBinaria(31, ArvoreBinaria(11, ArvoreBinaria(25, None, None), None), ArvoreBinaria(1, ArvoreBinaria(21, None, None), ArvoreBinaria(9, None, None))))
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(5, None, ArvoreBinaria(31, ArvoreBinaria(22, ArvoreBinaria(19, None, None), ArvoreBinaria(28, None, None)),
None))
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(2, None, ArvoreBinaria(3, None, ArvoreBinaria(17, ArvoreBinaria(11, None, None), ArvoreBinaria(27, None, None))))
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(19, ArvoreBinaria(2, ArvoreBinaria(26, ArvoreBinaria(4, None, None), ArvoreBinaria(14, None, None)), ArvoreBinaria(25, ArvoreBinaria(21, None, None), ArvoreBinaria(13, None, None))), None)
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(25, ArvoreBinaria(8, ArvoreBinaria(29, ArvoreBinaria(7, None, None), ArvoreBinaria(16, None, None)), ArvoreBinaria(30, None, ArvoreBinaria(19, None, None))), ArvoreBinaria(17, ArvoreBinaria(2, ArvoreBinaria(13, None, None), ArvoreBinaria(5, None, None)), ArvoreBinaria(23, ArvoreBinaria(18, None, None), ArvoreBinaria(0, None, None))))
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(31, ArvoreBinaria(30, ArvoreBinaria(13, ArvoreBinaria(4, None, None), ArvoreBinaria(18, None, None)), None), None)
print(constituiArvoreBinariaDeBusca(raiz))

#Results
#Teste 1: True
#Teste 2: True
#Teste 3: False
#Teste 4: True
#Teste 5:
# True
# False
# False
# True
# True
# True
# False
#Teste 6:
# False
# False
# True
# True
# False
# True
# True
# False
# False
# True