import datetime
import calendar


def generate_calendar(months_in_advance: int) -> list:
    current_date = datetime.date.today()
    current_month = current_date.month
    current_year = current_date.year
    full_calendar = calendar.HTMLCalendar()

    my_calendar = []
    for i in range(months_in_advance + 1):
        month_temp = (current_month + i) % 12
        if month_temp == 0:
            month = 12
        else:
            month = month_temp
        year = int(current_year + ((current_month + i - month) / 12))

        my_calendar.append(full_calendar.formatmonth(year, month))

    return my_calendar
