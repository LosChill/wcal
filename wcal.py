import pandas as pd
import datetime
import core
import functions

# Generate today's date
today = datetime.date.today()
current_year = today.year

# Call main function from core, creating calendar df, convert to strings
df = core.create_year_df(current_year)

# Remove Year column
del df['Year']

functions.header()

# Format and print dataframe from functions
functions.print_dataframe(df)
