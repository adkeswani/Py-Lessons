class SubCipher(object):
    def __init__(self, original, mixed):
        super(SubCipher,self).__init__()

sc = SubCipher("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz")
sc.decode(sc.encode("helloworld"))
