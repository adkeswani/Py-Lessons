class Parent(object):
    def __init__(self):
        print "Parent's init"

class Sub(Parent):
    def __init__(self):
        print "Sub's init"
        super(Sub, self).__init__()

Sub()
