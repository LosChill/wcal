import pandas
import datetime
import calendar
import wcal2
import textual

today = datetime.date.today()
current_year = today.year

df = wcal2.create_year_df(current_year)

print(df)
