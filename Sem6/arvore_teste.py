import math

class Node:
    def __init__(self, initValue, root=None, left=None, right=None):
        self.value = initValue
        self.root = root
        self.leftNode = left
        self.rightNode = right

    def getRoot(self):
        return self.root

    def getLeftNode(self):
        return self.leftNode

    def getRightNode(self):
        return self.rightNode

    def getValue(self):
        return self.value

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.level = 0
        self.isBalanced = False

    def __getRootNode(self):
        return self.root
    def getSize(self):
        return self.size

    def getLevels(self):
        return self.level if self.isBalanced else "The tree isn't balanced!"

    def getRoot(self):
        return self.root.value if self.root is not None else "There isn't a root!"

    # IN PROGRES --- --- --- --- --- --- --- ---
    # def __str__(self):
    #     printout = "("
    #     currentNode = self.root
    #
    #     for i in range(self.size):
    #
    #         while True:
    #             if currentNode is None:
    #
    #                 break
    #             current
    #
    #     # dir = True
    #     # nextNode = None
    #     # for i in range(self.size):
    #     #     if currentNode is None:
    #     #         break
    #     #     printout = printout + str(currentNode.value) + "(" if dir else printout
    #     #     if currentNode != nextNode:
    #     #         if currentNode.leftNode is not None:
    #     #             if currentNode.rightNode is not None:
    #     #                 nextNode = currentNode.rightNode.root
    #     #             currentNode = currentNode.leftNode if dir else currentNode.root
    #     #         elif currentNode.rightNode is not None:
    #     #             printout = printout + "()("
    #     #             currentNode = currentNode.rightNode if dir else currentNode.root
    #     #         else:
    #     #             dir = False
    #     #             printout = printout + "()())"
    #     #             currentNode = currentNode.root
    #
    #
    #     return printout + ')'

    def append(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__recursiveAppend(self.root, value)

        self.size += 1
        self.level = math.log2(self.size + 1)

    def __recursiveAppend(self, currentNode:Node, value):

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

    # def search(self,value,currentNode = self.__getRootNode()):
    #     #return the node of the value
    #     if value < currentNode.value:
    #         self.search(value,currentNode.leftNode)
    #     elif value > currentNode.value:
    #         self.search(value, currentNode.rightNode)
    #     else:
    #         return currentNode

    def left_rotation(self,currentNode:Node):
        temp = currentNode.rightNode
        currentNode.rightNode = temp.leftNode
        if temp.leftNode:
            temp.leftNode.root = currentNode
        temp.root = currentNode.root
        if currentNode.root is None:
            self.root = temp
        elif currentNode == currentNode.root.leftNode:
            currentNode.root.leftNode = temp
        else:
            currentNode.root.rightNode = temp
        temp.leftNode = currentNode
        currentNode.root = temp

    def right_rotation(self,currentNode:Node):
        temp = currentNode.leftNode
        currentNode.leftNode = temp.rightNode
        if temp.rightNode:
            temp.rightNode.root = currentNode
        temp.root = currentNode.root
        if currentNode.root is None:
            self.root = temp
        elif currentNode == currentNode.root.rightNode:
            currentNode.root.rightNode = temp
        else:
            currentNode.root.leftNode = temp
        temp.rightNode = currentNode
        currentNode.root = temp


def inOrder(node:Node):
    if node.leftNode:
        inOrder(node.leftNode)
    print(node.value, end=" ")
    if node.rightNode:
        inOrder(node.rightNode)

def inPreOrder(node:Node):
    print(node.value, end=" ")
    if node.leftNode:
        inPreOrder(node.leftNode)
    if node.rightNode:
        inPreOrder(node.rightNode)

def inPosOrder(node:Node):
    if node.leftNode:
        inPosOrder(node.leftNode)
    if node.rightNode:
        inPosOrder(node.rightNode)
    print(node.value, end=" ")

A = BinarySearchTree()
# A.append(20)
# A.append(10)
# A.append(8)
# A.append(15)
# A.append(7)
# A.append(9)
# A.append(4)
# A.append(6)
# A.append(5)
# A.append(22)
# A.append(21)
# A.append(24)
# A.append(23)
# A.append(26)

# A.append(20)
# A.append(15)
# A.append(22)
# A.append(21)
# A.append(23)
# A.append(17)
# A.append(16)
#
# node = A.search(15)

# for valor in [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90]:
#     A.append(valor)


A.append(4)
A.append(2)
A.append(1)
A.append(3)
A.append(6)
A.append(7)
A.append(5)


print(A.getSize())
print(A.getLevels())
print(A.getRoot())
inOrder(A.root)
print()
inPreOrder(A.root)
print()
inPosOrder(A.root)