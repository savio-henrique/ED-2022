class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def nosIguais(noEsq,noDir):
    if noEsq is None and noDir is None:
        return True
    if (noEsq is not None and noDir is None) or (noEsq is None and noDir is not None):
        return False
    if noEsq.dado != noDir.dado:
        return False
    if not nosIguais(noEsq.esq, noDir.dir):
        return False
    if not nosIguais(noEsq.dir, noDir.esq):
        return False

    return True

def verificaSimetria(no):
    if not no:
        return True
    return nosIguais(no.esq,no.dir)



#Testes
# Teste 1:
raiz = ArvoreBinaria(1, ArvoreBinaria(0, ArvoreBinaria(1), ArvoreBinaria(0)), ArvoreBinaria(0, ArvoreBinaria(0), ArvoreBinaria(1)))
print(verificaSimetria(raiz))
# Teste 2:
raiz = ArvoreBinaria(1, ArvoreBinaria(0, ArvoreBinaria(0), ArvoreBinaria(1)), ArvoreBinaria(0, ArvoreBinaria(0), ArvoreBinaria(1)))
print(verificaSimetria(raiz))
# Teste 3:
raiz = ArvoreBinaria(0, ArvoreBinaria(1, ArvoreBinaria(1, None, None), ArvoreBinaria(0, None, None)), ArvoreBinaria(1, ArvoreBinaria(1, None, None), ArvoreBinaria(0, None, None)))
print(verificaSimetria(raiz))

#Resultados
# Teste 1: True
# Teste 2: False
# Teste 3: False