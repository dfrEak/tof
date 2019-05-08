import numpy as np

class peak:
  '''
  # first(lag) window
  sumSetup = -1
  avgSetup = -1
  stdSetup = -1
  '''

  #moving filter
  #avgFilter=-1
  #stdFilter=-1
  filteredWindow=[]

  #parameter
  threshold=5
  influence=0.1
  stat=0

  def __init__(self, threshold, influence):
    self.threshold=threshold
    self.influence=influence

  def __init__(self, threshold, influence, filteredWindow):
    self.threshold = threshold
    self.influence = influence
    self.filteredWindow = filteredWindow

  def addSignalSetup(self, newData):
    self.filteredWindow.append(newData)

  def addSignal(self, newData):
    #remove first
    del self.filteredWindow[0]
    #add last
    self.filteredWindow.append(newData)

  '''
  def calculateAvgStd(self, first):
    self.sumFilter = np.sum(self.filteredWindow)
    self.avgFilter = np.average(self.filteredWindow)
    self.stdFilter = np.std(self.filteredWindow)
  '''

  def calculateStatus(self, range):
    #https://stackoverflow.com/questions/22583391/peak-signal-detection-in-realtime-timeseries-data
    #with some modifications
    sumFilter = np.sum(self.filteredWindow)
    avgFilter = np.average(self.filteredWindow)
    stdFilter = np.std(self.filteredWindow)

    retval=0

    if (abs(range - avgFilter) > self.threshold*stdFilter):
      if(range > avgFilter):
        retval = 1
        #print("Signal +1")
      else:
        retval = -1
        #print("Signal -1")
      pdFiltered = self.influence*range + (1-self.influence)*self.filteredWindow[len(self.filteredWindow)-1]
      self.addSignal(pdFiltered)
    else: #stream data not change that much
      retval = 0
      self.addSignal(range)
      #print("Signal 0")

    return(retval)

  def checkStability(self, range):
    newStat = calculateStatus(range)
    if (self.stat!=0 and newStat==0):
      self.stat = newStat
      return True
    else:
      self.stat = newStat
      return False


if __name__ == "__main__":
  pk = peak(5,0.1,[5,4,5,6,5,4,4,5,6,6,6,7,4,5,4])
  print(pk.calculateStatus(10))

