# room-booking-app
calendar view web app that lets users book a room and remembers which rooms are booked

Using a json file as a database for now. format: {"room_name":{"yyyy-mm-dd":("example@hotmail.com", number_of_nights_booked)}}

## To Do:

### forms.py
* add proper validators & fields for variables instead of all StringField

### server.py
* pass new booking from index.html to db.json

### calendar_script.js
* Add inner-date css class to dates between start and end date
* Add hover text to calendar for unavailable/past days
* Add alerts for whether booking succeeds, and when a range of dates with an included unavailable date is selected

### index.html
* Take form data from BookingForm and create a new booking
* Improve the page layout/style
    * Fix carousel indicator overlap with caledar
    * Change carousel to show multiple months for large displays