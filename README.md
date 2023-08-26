# room-booking-app
calendar view web app that lets users book a room and remembers which rooms are booked

Using a json file as a database for now. format: {"room_name":{"yyyy-mm-dd":("example@hotmail.com", number of nights booked)}}

## To Do:

### forms.py
* add proper validators & fields for variables instead of all StringField

### server.py
* pass new booking from index.html to db.json

### bookings.py
* add .past html class to calendar days before today

### calendar_script.js
* Make calendar interactable as an alternative to using the form
* Prevent unavailable & past dates from being selectable
* Add hover text to calendar for unavailable/past days
* Add alerts for whether booking succeeds

### index.html
* Take form data from BookingForm and create a new booking
* Improve the page layout/style
    * Fix carousel indicator overlap with caledar
    * Change carousel to show multiple months for large displays