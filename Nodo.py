
class Nodo:
    def __init__(self, value):
        self.element = value
        self.altura = None
        self.izq = None
        self.der = None
    def __init__(self, val, izq, der):
        self.element = val
        self.izq = izq
        self.der = der
        self.altura = None
    def getElement(self):
        return self.element
    def getIzq(self):
        return self.izq
    def getDer(self):
        return self.der

    def getAltura(self, a):
        if self.izq == None and self.der == None: self.altura = 0
        elif self.altura == None:
            self.altura = 1 + max(self.izq.getAltura(self.izq), self.der.getAltura(self.der))
        return self.altura

    def setIzq(self, i):
        self.izq = i
    def setDer(self, d):
        self.der = d
    def setElement(self, e):
        self.element= e

