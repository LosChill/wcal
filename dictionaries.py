import calendar
import datetime

"""Dictionaries for wcal abbreviations"""

# Set spacing constant
padnumber = 5

# Create dictionary of month abbreviations from calendar library
month_list = list(calendar.month_name)[1:]
month_abbrev = [month[:3] for month in month_list]
month_dict = {month: abbrev for month, abbrev in zip(month_list, month_abbrev)}

# Create dictionary of day abbreviations from calendar library
days_list = list(calendar.day_name)
days_abbrev = [day[:3] for day in days_list]

# Create month-number to color dictionary
color_dict = {1: 'red',
              2: 'light_red',
              3: 'yellow',
              4: 'light_yellow',
              5: 'green',
              6: 'light_green',
              7: 'blue',
              8: 'light_blue',
              9: 'magenta',
              10: 'light_magenta',
              11: 'cyan',
              12: 'light_cyan'
}

# Create month string to month number dictionary.
month_number_dict = {'Jan': 1,
                     'Feb': 2,
                     'Mar': 3,
                     'Apr': 4,
                     'May': 5,
                     'Jun': 6,
                     'Jul': 7,
                     'Aug': 8,
                     'Sep': 9,
                     'Oct': 10,
                     'Nov': 11,
                     'Dec': 12
}
