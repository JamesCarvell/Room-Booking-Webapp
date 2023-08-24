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
    expanded_bookings = []
    bookings_dict = read_bookings(database)
    for room in bookings_dict.keys():
        for booking_date in bookings_dict[room].keys():
            for day in range(bookings_dict[room][booking_date][1]):
                year = booking_date[:4]
                month = booking_date[4:6]
                day = booking_date[6:]
                expanded_bookings.append(datetime.date(booking_date) + datetime.timedelta(days=day))
    return expanded_bookings


def room_availability(expanded_bookings: list, room_count: int) -> list:
    count_by_date = collections.Counter(expanded_bookings)
    unavailable = [booking_date for booking_date in count_by_date.keys() if count_by_date[booking_date] >= room_count]
    return(unavailable)

print(expand_bookings("db.json"))
