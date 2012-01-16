class MyInt(object):
    def __init__(self, anInt):
        self.int = anInt

    def __repr__(self):
        return str(self.int)

    def __add__(self, other):
        return MyInt(self.int + other)
    
    def __sub__(self, other):
        return MyInt(self.int - other)
