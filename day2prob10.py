def next_day_yyyymmdd(year, month, day):
    """User will enter a year, month, and day of the month, and the
    function will print the following day (ignoring leap years).
    """

year = int(input("Enter a year(0-current): "))

month = int(input("Enter a month (1-12): "))

if month in (1, 3, 5, 7, 8, 10, 12):
    days_in_month = 31
elif month == 2:
    days_in_month = 28
else:
    days_in_month = 30

day = int(input("Enter a day (1-31): "))

if day < days_in_month:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

print("The next day is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))

