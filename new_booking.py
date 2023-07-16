""" Reads json data file, takes user input in terminal for a new booking, updates json and writes
over whole file. """
import json
import collections


def read_bookings(database):
    with open(database, "r", encoding="utf-8") as db:
        data_dict = json.load(db)
        return data_dict


def create_new_booking(database, new_booking):
    with open(database, "r+", encoding="utf-8") as db:
        data = json.load(db)
        data.update(new_booking)
        json.dump(data, db, indent=2)


expanded_bookings = []
bookings_dict = read_bookings("db.json")
for room in bookings_dict.keys():
    for booking_date in bookings_dict[room].keys():
        for day in range(bookings_dict[room][booking_date][1]):
            expanded_bookings.append(int(booking_date) + day)
count_by_date = collections.Counter(expanded_bookings)
unavailable = [booking_date for booking_date in count_by_date.keys() if count_by_date[booking_date] >= 10]
print(count_by_date)
print(unavailable)
