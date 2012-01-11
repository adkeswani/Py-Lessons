class Vehicle(object):
    def __init__(self, currSpeed, numWheels, inDisguise, modelName):
        self.currSpeed = currSpeed
        self.numWheels = numWheels
        self.inDisguise = inDisguise
        self.modelName = modelName

    def getMaxSpeed(self):
        maxSpeed = self.currSpeed ** 2
        maxSpeed = maxSpeed + 10
        maxSpeed = maxSpeed / 10
        maxSpeed = maxSpeed + self.currSpeed

        return maxSpeed

    def isTransformer(self):
        return self.inDisguise

    def printMe(self, printWheels, printModel, printTransformer, printMightBe, printSpeed):
        if printTransformer:
            if self.isTransformer():
                print "This vehicle is a transformer"
            else:
                print "This vehicle is not a transformer"

        if printModel:
            print self.modelName

        if printWheels:
            print "This vehicle has", self.numWheels, "wheels"

        if printSpeed:
            print "This vehicle is currently at speed", self.currSpeed, "and has a maximum speed", self.getMaxSpeed()

        if printMightBe:
            if self.numWheels == 2:
                print "This might be a bicycle"
            elif self.numWheels == 3:
                print "This might be a tricycle"
            elif self.numWheels == 4:
                print "This might be a monster truck"
            elif self.numWheels > 4:
                print "This might be something else"
            else:
                print "This might be a unicycle or a flying car"
