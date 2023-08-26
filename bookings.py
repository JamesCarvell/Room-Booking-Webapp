""" Reads json data file, takes user input in terminal for a new booking, updates json and writes
over whole file. """
import json
import collections
import datetime


def read_bookings(database) -> dict:
    with open(database, "r", encoding="utf-8") as db:
        data_dict = json.load(db)
        return data_dict


def create_new_booking(database, new_booking):
    with open(database, "r+", encoding="utf-8") as db:
        data = json.load(db)
        data.update(new_booking)
        json.dump(data, db, indent=2)


def expand_bookings(database) -> list:
    "convert bookings json data of first date of booking and number of nights booked to a list of date strings"
    expanded_bookings = []
    bookings_dict = read_bookings(database)
    for room in bookings_dict.keys():
        for first_date_of_booking in bookings_dict[room].keys():
            for previous_days_of_booking in range(bookings_dict[room][first_date_of_booking][1]):
                date_of_booking = datetime.date.fromisoformat(first_date_of_booking) + datetime.timedelta(days=previous_days_of_booking)
                expanded_bookings.append((date_of_booking.strftime("%B %Y"), str(int(date_of_booking.strftime("%d")))))
    return expanded_bookings


def room_availability(expanded_bookings: list, room_count: int) -> dict:
    count_by_date = collections.Counter(expanded_bookings)
    unavailable_list = [date for date in count_by_date.keys() if count_by_date[date] >= room_count]
    unavailable_dict = {}
    for date in unavailable_list:
        unavailable_dict.setdefault(date[0],[]).append(date[1])
    return(unavailable_dict)


# def list_past_dates():
#     past_dates = {}
#     current_date = datetime.date.today()
#     current_month = current_date.month
#     one_day = datetime.timedelta(days=1)
#     while current_date.month == current_month:
#         current_date -= one_day
#         past_dates.update(current_date.)
    

# print(room_availability(expand_bookings("db.json"),4))
