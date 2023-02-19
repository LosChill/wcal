#!/usr/bin/env python

import calendar
import datetime
from datetime import date
from termcolor import colored, cprint

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

colors = {1: "yellow", 2: "green", 3: "blue", 4: "cyan", 5: "magenta", 6: "white", 7: "light_red", 8: "light_green", 9: "light_yellow", 10: "light_blue", 11: "light_cyan", 12: "light_magenta"}

# Print header

print("Wk   Mon Tue Wed Thu Fri Sat Sun")

# Print calendar

for i in range(0, len(unique_cal_year), 7):                     # Iterate year to weeks
    week = unique_cal_year[i:i+7]                               # Iterate days of week
    year, month, day = week[0][0], week[0][1], week[0][2]       # Set year, moth, day variables
    isowk = datetime.date(year, month, day).isocalendar()       # Find ISO
    print("{:>2}".format(isowk[1]), end="   ")                  # Print ISO

    for day in week:                                            # Iterate through days
        color = colors.get(day[1], "light_grey")                # Get color based on month
        print(colored("{:>3}".format(day[2]), color), end=" ")  # Print day
    print()
