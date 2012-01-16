glob = "G"

class A(object):
    glob = "A"

    def __init__(self):
        print glob

a = A()
print glob
