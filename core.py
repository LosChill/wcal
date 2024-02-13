import calendar
import pandas as pd
import dictionaries

"""
This is the main calendar function:
It creates a dataframe of year with each iso week as a row.

The loop creates a month calendar as a list of weeks, where each week is represented as a list of datetime.date objects.
Each datetime.date object represents a day, ensuring weeks start on Monday..
This includes days from the preceding or next month to complete weeks at the start and end of the month.
Each week list of datetime.date objects is added to weeks_data.
Duplicate weeks will be removed on creation of dataframe.
This is repeaded for each month of the year.
"""

def create_year_df(current_year):

    # Create empty list of lists to accept columns
    weeks_data = []

    for month in range(1, 13):
        month_calendar = calendar.Calendar(firstweekday=calendar.MONDAY).monthdatescalendar(current_year, month)

        for week in month_calendar:
            if any(day.year == current_year for day in week):
                iso_week = week[3].isocalendar()[1]
                iso_year = week[3].isocalendar()[0]
                month_name = ""
                
                for day in week:
                    if day.day == 1:
                        month_name = dictionaries.month_dict[calendar.month_name[day.month]]
                        break
            
                weeks_data.append([iso_year, iso_week] + list(week) + [month_name])

    # Build columns names for use in df creation
    columns = ["Year", "Week"] + dictionaries.days_abbrev + ["Month"]

    # Create df from list of lists, columns.
    df = pd.DataFrame(weeks_data, columns = columns)

    # Remove duplicate weeks, reset index
    df = df.drop_duplicates(subset=["Year", "Week"]).reset_index(drop=True)

    return df
