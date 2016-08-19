from MerkleTree import *
from Crypto.Hash import SHA256

def mihash(m):
    return SHA256.new(m).digest()
# Funciones "dummy"
keynum = 0
def K():
    global keynum
    res = keynum
    keynum += 1
    return [str(res)+"x",str(res)+"y"]

def S(m, x):
    return m + "|C:|" + x

def V(m, sig, y):
    num = ""
    i = 0
    while i < len(y)-1:
        num += y[i]
        i += 1
    return sig == m + "|C:|" + num + "x"
# Generar un MerkleTree
Merky = MerkleTree(4,[K, S, V],mihash)
# Recuperar su raíz
root = Merky.get_pk()

# Funcion para imprimir (de forma muy simplifista) el árbol
def printTree(roo):
    if roo.getIzq() != None: printTree(roo.getIzq())
    print "(" + str(roo.getAltura()) + " - " + roo.getElement() + ") "
    if roo.getDer() != None: printTree(roo.getDer())

print Merky.sk
printTree(root)
print "\n\n"
# Obtener verificador (el firmador es parte del árbol, el verificador es un objeto aparte)
very = Merky.get_verifier()
mens = "mensaje"
#Imprimir firma e imprimir si se verifica
for i in range(16):
    firma = Merky.sign(mens + str(i))
    print firma
    print very.verify("mensaje" + str(i), firma)

print "\nDone"

