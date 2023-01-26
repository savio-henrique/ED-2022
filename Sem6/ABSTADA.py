class Node:
    def __init__(self, initValue, root=None, left=None, right=None):
        self.value = initValue
        self.root = root
        self.leftNode = left
        self.rightNode = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def append(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__recursiveAppend(self.root, value)

    def __recursiveAppend(self, currentNode: Node, value):

        if value < currentNode.value:
            if currentNode.leftNode is None:
                currentNode.leftNode = Node(value, root=currentNode)
            else:
                self.__recursiveAppend(currentNode.leftNode, value)
        elif value > currentNode.value:
            if currentNode.rightNode is None:
                currentNode.rightNode = Node(value, root=currentNode)
            else:
                self.__recursiveAppend(currentNode.rightNode, value)
        else:
            print('Error: The element already exists in the tree!')

#FUNCOES DE SERIALIZAÇAO
def inOrder(node: Node):
    if node is None:
        return
    if node.leftNode:
        inOrder(node.leftNode)
    print(node.value, end=" ")
    if node.rightNode:
        inOrder(node.rightNode)


def inPreOrder(node: Node):
    if node is None:
        return
    print(node.value, end=" ")
    if node.leftNode:
        inPreOrder(node.leftNode)
    if node.rightNode:
        inPreOrder(node.rightNode)


def inPosOrder(node: Node):
    if node is None:
        return
    if node.leftNode:
        inPosOrder(node.leftNode)
    if node.rightNode:
        inPosOrder(node.rightNode)
    print(node.value, end=" ")
#FUNCOES DE SERIALIZAÇAO

def main():
    Arvore = BinarySearchTree()

    while True:
        entrada = input()
        if entrada.isdigit():
            Arvore.append(int(entrada))
        elif entrada == 'in':
            inOrder(Arvore.root)
            print()
        elif entrada == 'pre':
            inPreOrder(Arvore.root)
            print()
        elif entrada == 'pos':
            inPosOrder(Arvore.root)
            print()
        elif entrada == 'quack':
            break

main()