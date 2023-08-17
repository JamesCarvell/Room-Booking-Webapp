import datetime
import calendar

BOOK_MONTHS_IN_ADVANCE = 6

current_date = datetime.date.today()
current_month = current_date.month
current_year = current_date.year
my_calendar = calendar.HTMLCalendar()

for i in range(BOOK_MONTHS_IN_ADVANCE + 1):
    month = current_month + i
    if month <= 12:
        print(my_calendar.formatmonth(current_year, month))
    else:
        print(my_calendar.formatmonth(current_year + 1, month - 12))
