#!/usr/bin/python
# Note Manually changed Feb 29 to March 1 to avoid leap year issues
# __AUTHOR__ = Dor Rondel for ABCTF 2016

from datetime import datetime

original_dates = []  # list of all original dates

# getting separate dates and populating original date list
with open("date.txt", "r") as f:
    for line in f:
        original_dates.append(line.strip('\n'))


new_dates = []

#adding one year to the dates
for date in original_dates:
    if date[-1] == '9' and date[-4:] == '1999':
        new_dates.append(date[:-4] + '2000')
    elif date[-1] == '9':
        new_dates.append(date[:-2] + str(int(date[-2:])+1))
    else:
        new_dates.append(date[:-1] + str(int(date[-1]) + 1))

# Converting new dates to time objects and extracting day
day_list = [datetime.strptime(date, "%B %d, %Y").weekday() for date in new_dates]

print("ABCTF{"+str(day_list.count(4))+"}") # 4 = Friday

#Flag = 194
