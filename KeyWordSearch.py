import pandas as pd

dataframe = pd.read_csv("data.csv")
entity_values = ['PayPal', 'Honey', 'human', 'God']
dataframe["Entity_Value"] = ''

for index in dataframe.index:
    for value in entity_values:
        if value in dataframe['Summary'][index]:
            dataframe['Entity_Value'][index] = value

nan_value = float("NaN")
dataframe.replace("", nan_value, inplace=True)

dataframe.to_csv("KeySearch.csv", index=False)
