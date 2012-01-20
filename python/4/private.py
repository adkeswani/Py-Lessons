class Answer(object):
    def __init__(self):
        super(Answer, self).__init__()

        self.__secret = 42

    def showSecret(self):
        return self.__secret

    def __changeSecret(self, newSecret):
        self.__secret = newSecret

    def incSecret(self):
        self.__changeSecret(self.__secret + 1)

class NewAnswer(Answer):
    def __changeSecret(self, newSecret):
        self.__secret = newSecret - 10
        
