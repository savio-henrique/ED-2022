class Node():
    def __init__(self,name):
        self.name = name
        self.connections = {}

    def __str__(self):
        return str(self.name)

    def __lt__(self, other):
        return self.name < other.name

class Graph():
    def __init__(self):
        self.nodes = []

    def findNode(self,name):
        for i in self.nodes:
            if i.name == name:
                return i
        return None
    def addNode(self,node:Node):
        if node not in self.nodes:
            self.nodes.append(node)

    def addConnection(self,node1: Node, node2: Node, weight):
        if node1 in self.nodes:
            node1.connections[node2] = weight
        else:
            print("Node not in graph!")

    def addBiConnection(self, node1: Node, node2: Node, weight):
        if node1 in self.nodes:
            node1.connections[node2] = weight
            node2.connections[node1] = weight
        else:
            print("Node not in graph!")
#Classe Definida#

def printMatriz(matriz):
    for linha in matriz:
        for coluna in linha:
            print(f"{coluna: 4d}",end='')
        print()

def matrizAdj(grafo:Graph,qtd_ver):
    matriz = [[0 for x in range(qtd_ver)] for x in range(qtd_ver)]
    for i in grafo.nodes:
        v1 = int(i.name) - 1
        for connection in i.connections:
            v2 = int(connection.name) - 1
            matriz[v1][v2] = int(i.connections[connection])
    return matriz


def main():
    qtd_ver, qtd_are, tipo = input().split()
    grafo = Graph()
    for i in range(int(qtd_are)):
        entrada = input().split()
        v1 = grafo.findNode(entrada[0])
        if v1 is None:
            grafo.addNode(Node(entrada[0]))
            v1 = grafo.findNode(entrada[0])
        v2 = grafo.findNode(entrada[1])
        if v2 is None:
            grafo.addNode(Node(entrada[1]))
            v2 = grafo.findNode(entrada[1])
        if tipo == "D":
            grafo.addConnection(v1, v2, entrada[2])
        elif tipo == "N":
            grafo.addBiConnection(v1, v2, entrada[2])

    printMatriz(matrizAdj(grafo, int(qtd_ver)))


main()