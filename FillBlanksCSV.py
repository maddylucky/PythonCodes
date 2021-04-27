import pandas as pd

# Import CSV into pandas DF Object
df = pd.read_csv("data.csv")

# check if CSV has any blank spaces
if df.isnull().values.any():
    # Replace them with NONE
    df = df.fillna("NONE")
    # Writing CSV from updated DF
    df.to_csv("modified_data.csv", index=False)

