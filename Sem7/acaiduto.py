class Node():
    def __init__(self, name):
        self.name = name
        self.connections = {}

    def addConnection(self, node, weight):
        if node not in self.connections:
            self.connections[node] = weight

    def __lt__(self, other):
        return self.name < other.name

class Graph():

    def __init__(self, name):
        self.name = name
        self.nodes = []

    def findNode(self, name):
        for i in self.nodes:
            if i.name == name:
                return i
        return None

    def addNode(self, node: Node):
        if node not in self.nodes:
            self.nodes.append(node)

    def addConnection(self, node1: Node, node2: Node, weight):
        if node1 in self.nodes and node2 in self.nodes:
            node1.addConnection(node2, weight)
        else:
            print("Node not in graph!")

    def addBiConnection(self, node1: Node, node2: Node, weight):
        if node1 in self.nodes and node2 in self.nodes:
            node1.addConnection(node2, weight)
            node2.addConnection(node1, weight)
        else:
            print("Node not in graph!")

def buscarVertice(partida, destino,distancia_vis=0, visitados = None):

    if visitados is None:
        visitados = [partida]
    if destino in visitados:
        return distancia_vis, visitados

    distanciaCurta = 9999999999999999999
    rotaCurta = None

    for vertice in partida.connections:

        if vertice in visitados:
            continue
        distancia_v = partida.connections[vertice]
        distancia, rota = buscarVertice(vertice,destino,distancia_vis+distancia_v,[*visitados,vertice])

        if distancia < distanciaCurta:
            distanciaCurta = distancia
            rotaCurta = rota

    return distanciaCurta, rotaCurta

def menorCaminho(graph: Graph):
    edges = []
    subgraph = Graph("Minimal")

    for node in graph.nodes:
        subgraph.addNode(Node(node.name))
        for node2 in node.connections:
            weight = node.connections[node2]
            edges.append((node.name, node2.name, weight))

    edges = list(sorted(edges, key=lambda x: x[2]))
    for edge in edges:
        v1 = subgraph.findNode(edge[0])
        v2 = subgraph.findNode(edge[1])
        trash, route = buscarVertice(v1, v2)
        if route is None:
            subgraph.addBiConnection(v1,v2,edge[2])

    return subgraph.nodes

def somarArestas(graph):
    vis_edges = {}
    for node in graph:
        for node2 in node.connections:
            vis_edges[(node, node2)] = node.connections[node2]
    return sum(vis_edges.values())/2

def main():
    qtd_casas = int(input())
    G = Graph("Vizinhança")
    for i in range(qtd_casas):
        entrada = input().split()
        casa1 = G.findNode(entrada[0])
        if casa1 is None:
            G.addNode(Node(entrada[0]))
            casa1 = G.findNode(entrada[0])
        qtd_viz = int(entrada[1])
        for i in range(qtd_viz):
            peso,vizinho = entrada[2+i*2:4+i*2]
            casa2 = G.findNode(vizinho)
            if casa2 is None:
                G.addNode(Node(vizinho))
                casa2 = G.findNode(vizinho)
            G.addBiConnection(casa1,casa2,int(peso))

    soma_distancia = somarArestas(menorCaminho(G))

    print(f"R$ {soma_distancia*3.14:.2f}")

main()
