import pandas as pd

def readFromCsv(file: str, dfColumn) -> pd.DataFrame:
    df = pd.read_csv(file, header=None)
    df.columns = dfColumn
    print(df.head())
    return df

def saveToCsv(filename: str, df: pd.DataFrame) -> None:
    print("save to csv")
    df.to_csv(filename=filename, index=False, encoding="utf-8")