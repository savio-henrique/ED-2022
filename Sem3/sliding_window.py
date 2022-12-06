class DeckElement:

    def __init__(self, initValue):
        self.value = initValue
        self.__next = None
        self.__previous = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.__next

    def get_previous(self):
        return self.__previous

    def set_value(self, newValue):
        if newValue is not None:
            self.value = newValue
        else:
            print("Valor Inválido!")

    def set_next(self, newNext):
        self.__next = newNext

    def set_previous(self, newPrevious):
        self.__previous = newPrevious

d = DeckElement(2)

print(d.value)

class Deck:
    def __init__(self):
        self.__size = 0
        self.__start = None
        self.__finish = None

    def __get_start(self):
        return self.__start

    def __get_finish(self):
        return self.__finish

    def get_size(self):
        return self.__size

    def search_by_index(self, index):
        if index <= (self.get_size() // 2):
            counter = 0
            newElement = self.__get_finish()
            while counter != index:
                newElement = newElement.get_next()
                counter += 1
        else:
            counter = self.get_size() - 1
            newElement = self.__get_start()
            while counter != index:
                newElement = newElement.get_previous()
                counter -= 1

        return newElement

    def queue(self, item, index=None):

        element = DeckElement(item)

        if self.get_size() == 0:
            self.__start = element
            self.__finish = element
            self.__size += 1
            return

        if index == 0:
            # Insert Element on Finish
            self.__get_finish().set_previous(element)
            element.set_next(self.__get_finish())
            self.__finish = element
        elif index is not None and index < self.get_size():
            # Insert Element on Index
            newElement = self.search_by_index(index)

            #Troca de referências
            newElement.get_previous().set_next(element)
            element.set_previous(newElement.get_previous())
            newElement.set_previous(element)
            element.set_next(newElement)

        else:
            self.__get_start().set_next(element)
            element.set_previous(self.__get_start())
            self.__start = element

        self.__size += 1

    def dequeue(self, index=None):
        if self.__get_start() is None:
            return None

        if index == 0:
            if self.__get_finish() is None:
                return None

            element = self.__finish
            self.__finish = self.__get_finish().get_next()
            element.set_next(None)
            if self.get_size() != 1:
                self.__get_finish().set_previous(None)

        elif index is not None and index < self.get_size():
            #Select the respective element on index
            element = self.search_by_index(index)

            element.get_next().set_previous(element.get_previous())
            element.get_previous().set_next(element.get_next())
            element.set_next(None)
            element.set_previous(None)

        else:
            element = self.__get_start()
            self.__start = element.get_previous()
            element.set_previous(None)
            self.__start.set_next(None)

        self.__size -= 1
        return element.get_value()

    def greater(self):
        counter = 0
        great = 0
        element = self.__get_finish()
        while counter != self.get_size():
            if element.get_value() > great:
                great = element.get_value()
            element = element.get_next()
            counter += 1

        return great

def main():
    deque = Deck()
    qtd_num = int(input())
    list_num = list(map(int,input().split()))
    size_janela = int(input())
    for n in range(size_janela):
        deque.queue(list_num[n])

    print(deque.greater(), end="  ")
    for i in range(qtd_num-(size_janela-1)-1):
        deque.dequeue(0)
        deque.queue(list_num[i + size_janela])
        print(deque.greater(), end="  ")

main()