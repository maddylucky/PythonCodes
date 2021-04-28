import pandas as pd

# Import CSV into pandas DF Object
df = pd.read_csv("data.csv")

# check if CSV has any blank spaces
if df.isnull().values.any():
    # Replace them with NONE
    df = df.fillna("NONE")

# Adding new column with value
df["New_Column"] = "STA"


# Rename Specific Columns
df.rename(columns={"name": "Name", " job": "Universe"}, inplace=True)

# Rename All Columns
df.columns = ['name', 'Universe', 'City', 'New'

# Writing CSV from updated DF
df.to_csv("modified_data.csv", index=False)
