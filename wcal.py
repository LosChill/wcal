import datetime
import calendar
import pandas as pd

def create_year_df(current_year):

    weeks_data = []

    for month in range(1, 13):
        month_calendar = calendar.Calendar(firstweekday=calendar.MONDAY).monthdatescalendar(current_year, month)

        for week in month_calendar:
            if any(day.year == current_year for day in week):
                iso_week = week[3].isocalendar()[1]
                iso_year = week[3].isocalendar()[0]
                days_of_month = [day.day for day in week]
                weeks_data.append([iso_year, iso_week] + days_of_month)

    days_list = ["Mon",
                "Tue",
                "Wed",
                "Thu",
                "Fri",
                "Sat",
                "Sun"]
    columns = ["Year", "Week"] + days_list

    df = pd.DataFrame(weeks_data, columns = columns)

    df = df.drop_duplicates(subset=["Year", "Week"]).reset_index(drop=True)

    return df
