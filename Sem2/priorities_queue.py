class QueueElement:
    def __init__(self,initValue,priority):
        self.value = initValue
        self.priority = priority
        self.next = None

class Queue:
    def __init__(self):
        self.size = 0
        self.start = None
        self.finish = None

    def sizeOf(self):
        return self.size

    def queue(self,value,priority):
        element = QueueElement(initValue=value,priority=priority)

        if self.start == None:
            self.start = element

        if self.finish != None:
            self.finish.next = element

        self.finish = element
        element.next = None
        self.size+=1

    def dequeue(self):
        if self.start == None:
            return None

        valor = self.start
        self.start = self.start.next
        valor.next = None
        self.size -=1
        return valor



def main():
    string = input().split()
    dicio = {}

    for i in range(int(len(string)/2)):
        if int(string[(2*i)+1]) not in dicio:
            dicio[int(string[(2*i)+1])] = [string[2*i]]
        else:
            dicio[int(string[(2*i)+1])].append(string[2*i])

    prioridades = Queue()
    index = 1
    while len(dicio)>0:
        if index in dicio:
            if len(dicio[index])>1:
                for l in dicio[index]:
                    prioridades.queue(l,index)
            else:
                prioridades.queue(dicio[index][0],index)

            dicio.pop(index)

        index+=1

    atividades_feitas = int(input())

    for i in range(atividades_feitas):
        prioridades.dequeue()

    print(f"Tamanho da fila: {prioridades.sizeOf()}")
    for i in range(prioridades.sizeOf()):
        item = prioridades.dequeue()
        print(f"Atividade: {item.value}, Prioridade: #{item.priority}")


main()