#ref: https://www.analyticsvidhya.com/blog/2019/01/introduction-time-series-classification/
import sys
sys.path.append('../')
from tools import tools
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class signalprocessing:

    def plot(self,file):
        read=tools.read(file)
        print (read[0])
        # Plot a section of the waveform.
        data1=np.array(tools.column(read,1), dtype=np.uint16)
        data2=np.array(tools.column(read,2), dtype=np.uint16)
        print(data1.shape)
        print(data2.shape)
        print(pd.Series(data1).describe())
        #plt.plot(data1[75000:100000])
        #plt.show()


if __name__ == "__main__":
    p=signalprocessing()
    p.plot("D:\\data\\b827ebc7cc12_1_TOF_20190802.txt")