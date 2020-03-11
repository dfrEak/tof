#ref: https://www.analyticsvidhya.com/blog/2019/01/introduction-time-series-classification/
import sys
from utils import readFromCsv, saveToCsv
sys.path.append('../')
from tools import tools
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from time import time


class signalprocessing:
    def __init__(self):
        pass

    def showTime(self):
        print(time()-self.start)
        self.start = time()

    def plot1(self,file):
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

    def generateMean(self, df: pd.DataFrame, lag: int) -> pd.DataFrame:
        df["mean"] = 0
        row = df.iloc[:, 0].count()
        row -= lag
        print(row)
        row=10000
        for i in range(row):
            df.loc[i, "mean"] = df.loc[i:i+lag, "s1"].mean()
        print(df.head())
        return df

    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        retvaldf = df
        #retvaldf["mean"] = retvaldf["s1"].apply(lambda x: )

    def convert(self, df: pd.DataFrame, lag: int) -> pd.DataFrame:
        retval = pd.DataFrame(columns=np.arange(lag))
        row = df.iloc[:, 0].count()
        row -= lag
        print(row)

        for i in range(row):
            temp=df.iloc[i:i+lag,1:5]
            temp.index=np.arange(lag)
            retval=retval.append(temp.T, ignore_index=True)
        print(retval.head())
        print(retval.describe())
        return retval

    def plot(self):
        plt.figure(figsize=(17, 8))
        plt.plot(self.df.s1)
        plt.plot(self.df.s2)
        plt.plot(self.df.s3)
        plt.plot(self.df.s4)
        plt.title('S1')
        plt.ylabel('distance')
        plt.xlabel('time')
        plt.grid(False)
        plt.show()
s

if __name__ == "__main__":
    p=signalprocessing()
    #p.plot("D:\\data\\b827ebc7cc12_1_TOF_20190802.txt")
    #print(p.df.head())

    dfColumn = ["time", "s1", "s2", "s3", "s4"]
    p.start = time()
    df = readFromCsv("D:\\data\\b827ebc7cc12_1_TOF_20190802.csv", dfColumn)
    #self.df = readFromCsv("/home/d_freak/Downloads/data/b827ebc7cc12_1_TOF_20190802.csv", self.dfColumn)
    df = df[100000:150000].reset_index(drop=True)
    df = df[43000:44000].reset_index(drop=True)

    print(df.describe())

    print(df.head())

    print(df.tail())

    p.showTime()

    df=p.convert(df, 5)
    #self.df.rename(columns = )

    #saveToCsv("D:\\data\\b827ebc7cc12_1_TOF_20190802_edit.csv",self.df)
    #saveToCsv("/home/d_freak/Downloads/data/b827ebc7cc12_1_TOF_20190802_edit.csv",self.df)
    #self.df = self.generateMean(self.df,25)
    #self.showTime()

    #self.plot()

