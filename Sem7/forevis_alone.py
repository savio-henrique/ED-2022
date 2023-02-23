class Node():
    def __init__(self,name):
        self.name = name
        self.connections = []

    def addConnection(self,node):
        if node not in self.connections:
            self.connections.append(node)

    def __lt__(self, other):
        return self.name < other.name

class Graph():

    def __init__(self,name):
        self.name = name
        self.nodes = []

    def findNode(self,name):
        for i in self.nodes:
            if i.name == name:
                return i
        return None

    def addNode(self,node:Node) :
        if node not in self.nodes:
            self.nodes.append(node)

    def addConnection(self, node1:Node, node2:Node):
        if node1 in self.nodes and node2 in self.nodes:
            node1.addConnection(node2)
        else:
            print("Node not in graph!")

    def addBiConnection(self, node1: Node, node2: Node):
        if node1 in self.nodes and node2 in self.nodes:
            node1.addConnection(node2)
            node2.addConnection(node1)
        else:
            print("Node not in graph!")

def buscarVertice(partida, destino,distancia_vis=0, visitados = list()):


    if visitados == []:
        visitados.append(partida)
    if destino in visitados:
        return distancia_vis, visitados

    distanciaCurta = 9999999999999999999
    rotaCurta = None

    for vertice in partida.connections:
        if vertice in visitados:
            continue

        distancia, rota = buscarVertice(vertice,destino,len(visitados)-1,[*visitados,vertice])

        if distancia < distanciaCurta:
            distanciaCurta = distancia
            rotaCurta = rota

    return distanciaCurta , rotaCurta


def main():
    qtd_ver = int(input())
    G = Graph("Social")
    for i in range(qtd_ver):
        entrada = input().split()
        ver1 = G.findNode(entrada[0])
        if ver1 is None:
            ver1 = Node(entrada[0])
            G.addNode(ver1)
        qtd_are = int(entrada[1])
        for id in entrada[2:]:
            ver2 = G.findNode(id)
            if ver2 is None:
                ver2 = Node(id)
                G.addNode(ver2)
            G.addConnection(ver1,ver2)
    my_id, celeb_id = input().split()
    partida = G.findNode(my_id)
    destino = G.findNode(celeb_id)

    distancia = buscarVertice(partida,destino)[0]
    if distancia ==9999999999999999999:
        print("Forevis alonis...")
    else:
        print(distancia)


main()