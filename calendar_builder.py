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


def add_html_class_by_date(html_calendar_months: list, dates: dict, added_class: str) -> list:
    dict_keys = list(dates.keys())
    new_calendar = []
    for calendar_month in html_calendar_months:
        new_month = calendar_month
        for key in dict_keys:
            if key in new_month:
                for day_temp in dates[key]:
                    old_string = f'">{day_temp}<'
                    new_string = f' {added_class}">{day_temp}<'
                    new_month = new_month.replace(old_string, new_string)
                dict_keys.remove(key)
                break
        new_calendar.append(new_month)
    return new_calendar


# import bookings
# calendar = generate_calendar(12)
# unavailable = bookings.room_availability(bookings.expand_bookings("db.json"),4)
# new_html_cal = add_html_class_by_date(calendar, unavailable, "unavailable")
# print(new_html_cal)