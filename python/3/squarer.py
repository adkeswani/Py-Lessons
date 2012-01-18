class Squarer(object):
    def __init__(self, i):
        super(Squarer, self).__init__()
        self.i = i
    
    def square(self):
        self.i = self.i ** 2
        
l = [Squarer(2), Squarer(3), Squarer(4)]

for s in l:
    s.square()
    print s.i
