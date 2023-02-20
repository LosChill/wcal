#!/usr/bin/env python

import calendar
import datetime
from termcolor import colored, cprint

# Establish a string for today. Remove leaing zeros.

today_zeros = str(datetime.datetime.now().date())
y, m, d = today_zeros.split("-")
m = str(int(m))
d = str(int(d))
today = "-".join([y, m, d])

# Create list of day tuples (year, month, date, weekday)

cal = calendar.Calendar()
months = list(range(1, 13))
cal_year = []
for month in months:
    cal_month = list(cal.itermonthdays4(2023, month))
    cal_year.append(cal_month)
cal_year = [item for sublist in cal_year for item in sublist]

# Remove duplicate weeks

unique_cal_year = []
for day in cal_year:
    if day not in unique_cal_year:
        unique_cal_year.append(day)

# Set color dictionary

colors = {
    1: "cyan",
    2: "light_cyan",
    3: "green",
    4: "light_green",
    5: "light_yellow",
    6: "yellow",
    7: "light_red",
    8: "red",
    9: "light_magenta",
    10: "magenta",
    11: "light_blue",
    12: "blue",
}

# Set month dictionary

monthkey = {
    1: "jan",
    2: "feb",
    3: "mar",
    4: "apr",
    5: "may",
    6: "jun",
    7: "jul",
    8: "aug",
    9: "sep",
    10: "oct",
    11: "nov",
    12: "dec",
}

# Print header

cprint("Wk   Mon Tue Wed Thu Fri Sat Sun",
       "black", "on_white", attrs=["bold", "dark"])

# Print calendar

# Print ISO week
for i in range(0, len(unique_cal_year), 7):
    week = unique_cal_year[i:i+7]
    year, month, day = week[0][0], week[0][1], week[0][2]
    isowk = datetime.date(year, month, day).isocalendar()
    print("{:>2}".format(isowk[1]), end="   ")

    # Check if date is today. Print dates.
    for day in week:
        date_check = f"{day[0]}-{day[1]}-{day[2]}"
        if date_check != today:
            color = colors.get(day[1], "light_grey")
            print(colored("{:>3}".format(day[2]), color), end=" ")
        else:
            print("", end=" ")
            cprint("{:>2}".format(day[2]),
                   "black", "on_yellow", attrs=["bold", "dark"], end=" ")

    # Check if new month. Print month.
    week_check = [tuple[2] for tuple in week]
    if 8 in week_check:
        print(colored(f"  {monthkey[month]}", color, attrs=["bold"]))
    else:
        print()
