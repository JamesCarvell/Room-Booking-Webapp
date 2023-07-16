# room-booking-app
calendar view web app that lets users book a room and remembers which rooms are booked

Using a json file as a database for now. format: {"room##":{"yyyymmdd":("example@hotmail.com",N)}} ## is the room
number, N is the number of nights booked.

## To Do:

### forms.py
* add proper validators & fields for variables instead of all StringField

### server.py
* Determine current date
* Create calendars for current & next 12 months
* Determine fully booked dates
* Color code dates on calendars based on availability
* Create carousel showing two months; only manually scroll
* Take form data from BookingForm and create a new booking