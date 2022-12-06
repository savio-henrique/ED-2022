class StackElement:
    def __init__(self,initValue):
        self.value = initValue
        self.previous = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def sizeOf(self):
        return self.size

    def stack(self,value):
        element = StackElement(initValue=value)

        if (self.top != None):
            element.previous = self.top

        self.top = element
        self.size+=1

    def destack(self):
        if (self.top == None):
            return None

        element = self.top

        self.top = self.top.previous
        self.size-=1
        return element.value


def main():
    anilhas = Stack()
    while True:
        peso= int(input())
        if peso == 0:
            break
        anilhas.stack(peso)
    tirar = int(input())
    soma = 0
    contagem = 0
    while True:
        valor = anilhas.destack()
        if valor == None:
            print(f"Anilhas retiradas: {contagem}")
            print(f"Peso total movimentado: {soma}")
            break
        soma += valor
        contagem += 1
        if valor == tirar:
            print(f"Peso retirado: {valor}")
            print(f"Anilhas retiradas: {contagem}")
            print(f"Peso total movimentado: {soma}")
            break
        print(f"Peso retirado: {valor}")


main()