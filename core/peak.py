import numpy as np
import configparser


class peak:

    #def __init__(self, setupCount=10, threshold=5, influence=0.1):
    def __init__(self):
        print("peak init")
        '''
        # first(lag) window
        sumSetup = -1
        avgSetup = -1
        stdSetup = -1
        '''

        # moving filter
        self.avgFilter=-1
        # stdFilter=-1
        self.filteredWindow = []

        # parameter
        config = configparser.ConfigParser()
        #config.read('../conf.ini')
        config.read('conf.ini')
        self.setupCount = float(config['PEAK']['SETUP_COUNT'])
        self.threshold = float(config['PEAK']['THRESHOLD'])
        self.influence = float(config['PEAK']['INFLUENCE'])

        #self.setupCount = setupCount
        #self.threshold = threshold
        #self.influence = influence
        self.stat = 0

    def setFilteredWindow(self, filteredWindow):
        self.filteredWindow = filteredWindow

    def setSetupCount(self, setupCount):
        self.setupCount = setupCount

    def setThreshold(self, threshold):
        self.threshold = threshold

    def setInfluence(self, influence):
        self.influence = influence

    def getAvgFilter(self):
        self.avgFilter = np.average(self.filteredWindow)
        return self.avgFilter
    
    def getData(self,n):
        return self.filteredWindow[n]
    
    def getLastData(self):
        if(len(self.filteredWindow)!=0):
            return self.filteredWindow[len(self.filteredWindow)-1]
        else:
            return -1

    def getStat(self):
        return self.stat

    def addSignal(self, newData):
        #print("add signal")
        if (self.isReady()):  # check whether already full
            # remove first
            del self.filteredWindow[0]

        # add last
        self.filteredWindow.append(newData)

    def isReady(self):
        if (len(self.filteredWindow) > self.setupCount):  # check whether already full
            return True
        else:
            return False

    '''
    def calculateAvgStd(self, first):
      self.sumFilter = np.sum(self.filteredWindow)
      self.avgFilter = np.average(self.filteredWindow)
      self.stdFilter = np.std(self.filteredWindow)
    '''

    def calculateStatus(self, range):
        # https://stackoverflow.com/questions/22583391/peak-signal-detection-in-realtime-timeseries-data
        # with some modifications
        sumFilter = np.sum(self.filteredWindow)
        avgFilter = np.average(self.filteredWindow)
        stdFilter = np.std(self.filteredWindow)

        retval = 0

        if (abs(range - avgFilter) > self.threshold * stdFilter):
            if (range > avgFilter):
                retval = 1
                # print("Signal +1")
            else:
                retval = -1
                # print("Signal -1")
            pdFiltered = self.influence * range + (1 - self.influence) * self.filteredWindow[
                len(self.filteredWindow) - 1]
            self.addSignal(pdFiltered)
        else:  # stream data not change that much
            retval = 0
            self.addSignal(range)
            # print("Signal 0")

        # save the average
        self.avgFilter = avgFilter
        return (retval)

    def checkStability(self, range):
        newStat = calculateStatus(range)
        if (self.stat != 0 and newStat == 0):
            self.stat = newStat
            return True
        else:
            self.stat = newStat
            return False


if __name__ == "__main__":
    pk = peak()
    pk.setFilteredWindow([5, 4, 5, 6, 5, 4, 4, 5, 6, 6, 6, 7, 4, 5, 4])
    print(pk.calculateStatus(10))
    print(pk.getAvgFilter())
