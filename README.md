# room-booking-app
calendar view web app that lets users book a room and remembers which rooms are booked

Using a json file as a database for now. format: {"room_name":{"yyyy-mm-dd":("example@hotmail.com", number_of_nights_booked)}}

## To Do:

* Choose a room for booking & shuffle future bookings if needed
* Change duration to not include start date (one night stay duration = 0)

### forms.py
* Add proper validators & fields for variables instead of all StringField

### calendar_script.js
* Add inner-date css class to dates between start and end date
* Add hover text to calendar for unavailable/past days

### index.html
* Improve the page layout/style
    * Fix carousel indicator overlap with caledar
    * Change carousel to show multiple months for large displays