# room-booking-app
calendar view web app that lets users book a room and remembers which rooms are booked

Using a json file as a database for now. format: {"room##":{"yyyymmdd":("example@hotmail.com",N)}} ## is the room
number, N is the number of nights booked.

## To Do:

### forms.py
* add proper validators & fields for variables instead of all StringField

### server.py
* pass new booking from index.html to db.json

### index.html
* Color code dates on calendars based on availability
* Make calendar interactable as an alternative to using the form
* Prevent fully booked dates from being selectable
* Take form data from BookingForm and create a new booking
* Add alerts for whether booking succeeds
* Improve the page layout/style
    * Fix carousel indicator overlap with caledar
    * Add a legend and/or hover text to calendar to indicate meaning of different colors
    * Change carousel to show multiple months