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
        booking_room_key = next(iter(new_booking))
        booking_date_key = next(iter(new_booking[booking_room_key]))
        data[booking_room_key][booking_date_key] = new_booking[booking_room_key][booking_date_key]
        db.seek(0)
        json.dump(data, db, indent=2)
        db.truncate()


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


def check_room_availability(expanded_bookings: list, room_count: int) -> dict:
    count_by_date = collections.Counter(expanded_bookings)
    unavailable_list = [date for date in count_by_date.keys() if count_by_date[date] >= room_count]
    unavailable_dict = {}
    for date in unavailable_list:
        unavailable_dict.setdefault(date[0],[]).append(date[1])
    return unavailable_dict


def collect_past_dates():
    current_date = datetime.date.today()
    current_day = current_date.day
    key = current_date.strftime("%B %Y")
    past_dates = {key: list(range(1, current_day))}
    return past_dates
    

# print(room_availability(expand_bookings("db.json"),4))
