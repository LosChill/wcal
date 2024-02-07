# Dictionaries for wcal abbreviations
import calendar
import datetime

# Create list of month abbreviations from calendar library
month_list = list(calendar.month_name)[1:]
month_abbrev = [month[:3] for month in month_list]
month_dict = {month: abbrev for month, abbrev in zip(month_list, month_abbrev)}

# Create list of day abbreviations from calendar library
days_list = list(calendar.day_name)
days_abbrev = [day[:3] for day in days_list]

