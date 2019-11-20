#ref: https://www.analyticsvidhya.com/blog/2019/01/introduction-time-series-classification/
import sys
sys.path.append('../')
from tools import tools
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

class signalprocessing:
    def __init__(self):
        self.start = datetime.now()
        self.df = self.readFromCsv("D:\\data\\b827ebc7cc12_1_TOF_20190802.csv")
        self.df = self.df[100000:150000].reset_index(drop=True)
        self.df = self.df[100:300].reset_index(drop=True)

        print(self.df.head())

        self.showTime()

        self.df = self.generateMean(self.df,25)
        self.showTime()

        self.plot()

    def showTime(self):
        print(datetime.now()-self.start)
        self.start = datetime.now()

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

    def readFromCsv(self, file: str) -> pd.DataFrame:
        df = pd.read_csv(file, header = None)
        dfColumn = ["time","s1","s2","s3","s4"]
        df.columns = dfColumn
        print(df.head())

        return df

    def generateMean(self, df: pd.DataFrame, lag: int) -> pd.DataFrame:
        df["mean"] = 0
        row = df.iloc[:, 0].count()
        row -= lag
        print(row)
        row=10000
        for i in range(row):
            df.loc[i, "mean"] = df.loc[i:i + lag, "s1"].mean()
        print(df.head())
        return df

    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        retvaldf = df
        #retvaldf["mean"] = retvaldf["s1"].apply(lambda x: )

    def plot(self):
        plt.figure(figsize=(17, 8))
        plt.plot(self.df.s1)
        plt.title('S1')
        plt.ylabel('distance')
        plt.xlabel('time')
        plt.grid(False)
        plt.show()

if __name__ == "__main__":
    p=signalprocessing()
    #p.plot("D:\\data\\b827ebc7cc12_1_TOF_20190802.txt")
    #print(p.df.head())

