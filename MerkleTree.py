import math
import Nodo

class MerkleTree:
    # h = altura del arbol. Numero de hojas = 2^h -1
    # otsScheme = lista de algoritmos del one-time-signature scheme seleccionado
    #   La lista esta en la forma [K,S,V]
    # g = hashing usado
    def __init__(self, h, otsScheme , g):
        self.pk = ''
        self.sk = []
        leaves = []
        #Merkle Generation:
        for i in range(math.pow(2,h)-1):
            currentPair = otsScheme[0]()
            node1 = Nodo(g(currentPair[0]))
            self.sk.append(currentPair)
            stack = []
            while stack and (node1.getAltura() == stack[len(stack) - 1]):
                node2 = stack.pop()
                valNodo = g(node1.getElement()+node2.getElement())
                node1 = Nodo(valNodo, node2, node1)
            stack.append(node1)
        self.pk = stack.pop()

    def getPk(self):
        return self.pk



