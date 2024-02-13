import datetime
import dictionaries
from termcolor import cprint

"""
Functions for formatting, coloring, and printing the calendar dataframe.
"""

# Header Function. Spacing and printing header. Uses padding function
def header():
    columns_header = ["Week"] + dictionaries.days_abbrev + ["Month"]
    for column in columns_header:
        if column == 'Week':
            cprint(f"{column:>{dictionaries.padnumber}}", 'black', 'on_green', end='')
        elif column == 'Month':
            cprint(f"{column:>{dictionaries.padnumber}}", 'black', 'on_green', end='')
        else:
            cprint(f"{column:>{dictionaries.padnumber}}", 'black', 'on_blue', end='')
    print()

# Printing Cells Function. Spacing, coloring, and printing.
def print_dataframe(df):
    for index, row in df.iterrows():
        for col in df.columns:
            cell_value = row[col]
            if isinstance(cell_value, datetime.date):
                month = cell_value.month
                color = dictionaries.color_dict[month]
                if cell_value == datetime.date.today():
                    highlight = 2
                    spacer = ' ' * (dictionaries.padnumber - highlight)
                    print(spacer, end='')
                    cprint(f"{cell_value.day:>{highlight}}", 'black', 'on_yellow', end='')
                else:
                    color = dictionaries.color_dict[month]
                    cprint(f"{cell_value.day:>{dictionaries.padnumber}}", color, end='')
            elif isinstance(cell_value, int):
                print(f"{cell_value:>{dictionaries.padnumber}}", end='')
            elif cell_value in dictionaries.month_number_dict:
                color = dictionaries.color_dict[dictionaries.month_number_dict[cell_value]]
                cprint(f"{cell_value:>{dictionaries.padnumber}}", color)
            else:
                print()
