# Semana 3 - Deque e Lista :book:

-- --

## sliding_window.py

**O programa retorna o maior valor de dentro de uma janela deslizante dentro de uma lista de numeros.**

### *Input*

> O programa recebe 3 *inputs*, sendo o primeiro a quantidade de numeros existentes dentro da lista, 
> em seguida a lista em si, com seus elementos separados por um espaço em branco e, o ultimo *input*, o tamanho da janela.
> O input tem o seguinte formato:
> ```
> 9 
> 10 15 7 8 11 20 27 30 
> 3 
> ```

### *Output*

> O retorno esperado sao os maiores numeros de cada janela, utilizando o *input* de exemplo, nesse formato:
> ```
> 15  15  11  12  20  27  30
> ```

-- --

## list_inversion.py

**Desenvolva uma função, chamada *inverterLista()*, cujo reverta a ordem de uma lista não ordenada, utilizando a seguinte classe:**

```python
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        tmp = self.head
        lstr = ''
        while tmp != None:
            lstr += str(tmp.data) + ' '
            tmp = tmp.getNext()

        return lstr

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
```

### *Input*

> O programa não recebe nenhum *input* em especifico, somente uma serie de instruçoes, como por exemplo:
> ```python
> L = UnorderedList()
>
> L.add(2)
> L.add(3)
> L.add(2)
> L.add(5)
> 
> L = inverterLista(L)
> 
> print(L)
>```

### *Output*

> O retorno esperado depende da lista de instruçoes passadas, como por exemplo, utilizando as instruçoes acima como exemplo:
> ``` 
> [5, 2, 3, 2]
> ```