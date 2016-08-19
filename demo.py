from MerkleTree import *
keynum = 0
def K():
    global keynum
    res = keynum
    keynum += 1
    return str(res)
print "hola"
for i in range(10):
    print K()

def hasho(m):
    return "hasho! " + m



