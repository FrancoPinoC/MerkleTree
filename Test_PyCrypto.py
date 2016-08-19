from Crypto.Hash import SHA256

print "Holaaaaaa!"
h = SHA256.new()
h.update('hello')
print str(h.hexdigest())
