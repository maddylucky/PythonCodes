import pandas as pd

std_URL = "http://google.com/" //Use your defalt URL here

dataframe = pd.read_csv("data.csv")
dataframe["URL"] = ''

for index in dataframe.index:
    URL = std_URL + dataframe['name'][index]
    dataframe["URL"][index] = URL

dataframe.to_csv("output.csv", index=False)
