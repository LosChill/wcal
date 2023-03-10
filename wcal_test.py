#!/usr/bin/env python
# coding: utf-8

# In[8]:


import calendar
import datetime
from datetime import date
from termcolor import colored, cprint


# In[9]:


today = str(datetime.datetime.now().date())


# In[10]:


cal = calendar.Calendar()
months = list(range(1,13))
cal_year = []
for month in months:
    cal_month = list(cal.itermonthdays4(2023, month))
    cal_year.append(cal_month)
cal_year = [item for sublist in cal_year for item in sublist]


# In[11]:


unique_cal_year = []
for day in cal_year:
    if day not in unique_cal_year:
        unique_cal_year.append(day)


# In[12]:


colors = {1: "yellow", 2: "green", 3: "blue", 4: "cyan", 5: "magenta", 6: "white", 7: "light_red", 8: "light_green", 9: "light_yellow", 10: "light_blue", 11: "light_cyan", 12: "light_magenta"}


# In[13]:


print("Wk   Mon Tue Wed Thu Fri Sat Sun")

for i in range(0, len(unique_cal_year), 7):
    week = unique_cal_year[i:i+7]
    year, month, day = week[0][0], week[0][1], week[0][2]
    isowk = datetime.date(year, month, day).isocalendar()
    print("{:>2}".format(isowk[1]), end="   ")

    for day in week:
        date_check = f"{day[0]}-{day[1]}-{day[2]}"
        if date_check != today:
            color = colors.get(day[1], "light_grey")
            print(colored("{:>3}".format(day[2]), color), end=" ")
        else:
            cprint("{:>3}".format(day[2]), "black", "on_cyan", end=" ")
    print()


# In[14]:


time = datetime.datetime.now().date()
print(time)


# In[15]:


str(time)
print(time)


# In[ ]:




