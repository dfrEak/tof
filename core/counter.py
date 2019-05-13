from numba.cuda import selp
from peak import peak

class counter:

    def __init__(self, sensorNum=2, upperLimit=1500, lowerLimit=500):
        print("counter init")

        # threshold
        self.upperLimit = upperLimit
        self.lowerLimit = lowerLimit

        self.sensorList = []
        for x in range(sensorNum):
            self.sensorList.append(peak())
        #peak1 = peak()
        #peak2 = peak()


    def addSignal(self, sensor, range):
        self.sensorList[sensor].addSignal(range)
        print("add " + str(range) + " to peak" + str(sensor))
        print(self.sensorList[sensor].filteredWindow)
        '''
        if (sensor == 1):
            self.peak1.addSignal(range)
            print("add "+str(range)+" to peak1")
        elif (sensor == 2):
            self.peak2.addSignal(range)
            print("add "+str(range)+" to peak2")
        '''


    def checkInLimit(self, sensor):
        if (self.sensorList[sensor].getAvgFilter() >= self.lowerLimit) and (self.sensorList[sensor].getAvgFilter() <= self.upperLimit):
        #if (self.peak1.getAvgFilter() >= self.lowerLimit) and (self.peak2.getAvgFilter() <= self.upperLimit):
            return True
        else:
            return False

    def checkDetection(self):
        if (True):
            return True
        else:
            return False

if __name__ == "__main__":
    co = counter()
    co.addSignal(0,22)
    co.addSignal(1,503)
    print(co.checkInLimit(0))
    print(co.checkInLimit(1))
    print(co.sensorList)
    print(co.checkDetection())

    '''
    co = counter()
    co.addSignal(1,22)
    co.addSignal(2,503)
    print(co.checkInLimit(1))
    print(co.checkInLimit(2))
    print(co.peak1.filteredWindow)
    print(co.peak2.filteredWindow)
    '''