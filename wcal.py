import pandas as pd
import datetime
import core
import dictionaries

today = datetime.date.today()
current_year = today.year

# Call main function from core, convert to strings
df = core.create_year_df(current_year).astype(str)

# Remove Year column
del df["Year"]

# Spacing and printing header --> Header function, Padding function
columns_to_print = ["Week"] + dictionaries.days_abbrev + ["Month"]
columns_padded = [column + ' ' * (6 - len(column)) for column in columns_to_print]
columns_string = "".join(columns_padded)

print(columns_string)

# Reading rows from df, spacing, and printing --> Field function, Padding function
def format_dataframe(df):
    for index in range(len(df.index)):
        row = df.loc[index].tolist()
        row_padded = [cell + ' ' * (6 - len(cell)) for cell in row]
        row_string = "".join(row_padded)
        print(row_string)


test = format_dataframe(df)
print(test)
