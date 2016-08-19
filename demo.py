from MerkleTree import *
from Crypto.Hash import SHA256

print "Holaaaaaa!"

def mihash(m):
    return SHA256.new(m).digest()
print mihash("mensaje")
print mihash("mensaje")
keynum = 0

def K():
    global keynum
    res = keynum
    keynum += 1
    return [str(res)+"x",str(res)+"y"]

#def hasho(m):
#    return "hasho! " + m + " "

def S(m, x):
    return m + "|C:|" + x

def V(m, sig, y):
    num = ""
    i = 0
    while i < len(y)-1:
        num += y[i]
        i += 1
    return sig == m + "|C:|" + num + "x"

Merky = MerkleTree(3,[K, S, V],mihash)
root = Merky.get_pk()
def printTree(roo):
    if roo.getIzq() != None: printTree(roo.getIzq())
    print "(" + str(roo.getAltura()) + " - " + roo.getElement() + ") "
    if roo.getDer() != None: printTree(roo.getDer())

print Merky.sk
printTree(root)
print "\n\n"
very = Merky.get_verifier()
mens = "mensaje"
for i in range(8):
    firma = Merky.sign(mens)
    print firma
    print very.verify("mensaje", firma)
print "AAAA"

