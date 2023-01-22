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

    def left_rotation(self,currentNode:Node):
        temp = currentNode.rightNode



A = BinarySearchTree()
A.append(20)
A.append(10)
A.append(8)
A.append(15)
A.append(7)
A.append(9)
A.append(4)
A.append(6)
A.append(5)
A.append(22)
A.append(21)
A.append(24)
A.append(23)
A.append(26)

print(A.getSize())
print(A.getLevels())
print(A.getRoot())