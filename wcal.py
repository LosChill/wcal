import pandas as pd
import datetime
import core

today = datetime.date.today()
current_year = today.year

df = core.create_year_df(current_year)

print(df)
