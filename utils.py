from datetime import datetime, date, timedelta


def number_of_leap_years(from_date) -> int:
    now = date.today()
    leap_years = 0

    while from_date < now:
        if from_date.year % 4 == 0:
            leap_years += 1

        from_date = date(from_date.year+1, from_date.month, from_date.day)

    return leap_years
