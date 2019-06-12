#from numba.cuda import selp

from .peak import peak

class counter:

    def __init__(self, sensorNum=2, upperLimit=1500, lowerLimit=500):
        print("counter init")

        # threshold
        self.upperLimit = upperLimit
        self.lowerLimit = lowerLimit

        # list of sensors
        self.sensorList = []
        self.counter = []
        for x in range(sensorNum):
            self.sensorList.append(peak())
            # counter
            self.counter.append(0)
        #peak1 = peak()
        #peak2 = peak()

        # detected status
        self.detectedStat = 0





    def addSignal(self, sensor, range):
        self.sensorList[sensor].addSignal(range)
        #print("add " + str(range) + " to peak" + str(sensor))
        #print(self.sensorList[sensor].filteredWindow)
        '''
        if (sensor == 1):
            self.peak1.addSignal(range)
            print("add "+str(range)+" to peak1")
        elif (sensor == 2):
            self.peak2.addSignal(range)
            print("add "+str(range)+" to peak2")
        '''

    def checkInLimit(self, sensor):
        # using avg
        #if (self.sensorList[sensor].getAvgFilter() >= self.lowerLimit) and (self.sensorList[sensor].getAvgFilter() <= self.upperLimit):
        # using real range
        if (self.sensorList[sensor].getLastData() >= self.lowerLimit) and (self.sensorList[sensor].getLastData() <= self.upperLimit):
        #if (self.peak1.getAvgFilter() >= self.lowerLimit) and (self.peak2.getAvgFilter() <= self.upperLimit):
            return True
        else:
            return False

    def checkDetection(self): # return -1 when object detected in every sensors
        for x in range(len(self.sensorList)):
            if (not self.checkInLimit(x)):
                return False
        return True

    def updateDetectionStat(self):
        if (self.checkDetection()): # detected: all sensors in limit
            self.detectedStat = 1
        else:
            self.detectedStat = 0

    def checkMovementAdd(self, sensor, range):
        retval = -1
        self.addSignal(sensor, range)
        if (self.sensorList[len(self.sensorList)-1].isReady()):
            if (self.detectedStat == 1):
                print("detected")
                if (not self.checkInLimit(sensor)): # if sensor not in limit
                    retval = (1-sensor) # in case of 2 sensors
        # update detection stat
        self.updateDetectionStat()

        # add counter
        if (retval == 0):
            self.counter[0]+=1
        elif (retval == 1):
            self.counter[1]+=1
        return retval

if __name__ == "__main__":
    co = counter()
    co.addSignal(0,555)
    co.addSignal(1,503)
    print(co.checkInLimit(0))
    print(co.checkInLimit(1))
    print(co.sensorList)
    print(co.checkDetection())
    print(co.checkMovementAdd(0, 520))
    print(co.checkMovementAdd(1, 500))
    print(co.checkMovementAdd(0, 300))

    '''
    co = counter()
    co.addSignal(1,22)
    co.addSignal(2,503)
    print(co.checkInLimit(1))
    print(co.checkInLimit(2))
    print(co.peak1.filteredWindow)
    print(co.peak2.filteredWindow)
    '''