"""main file running webapp"""
import flask
from flask_bootstrap import Bootstrap
from forms import BookingForm
import calendar_builder
import bookings
import datetime


SEE_MONTHS_IN_ADVANCE = 12
ROOM_COUNT = 4


app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"
Bootstrap(app)


@app.route('/', methods=["GET", "POST"])
def index():
    booking = BookingForm()
    if booking.validate_on_submit():
        email = booking.email.data
        start_date_string = booking.start_date.data
        start_date = datetime.date.fromisoformat(start_date_string)
        end_date_string = booking.end_date.data
        end_date = datetime.date.fromisoformat(end_date_string)
        duration_timedelta = end_date - start_date
        duration_int = int(duration_timedelta.total_seconds() / (60 * 60 * 24)) + 1
        new_booking = {"room06": {start_date_string: [email, duration_int]}}
        bookings.create_new_booking("db.json", new_booking)
    
    calendar = calendar_builder.generate_calendar(SEE_MONTHS_IN_ADVANCE)
    unavailable = bookings.check_room_availability(bookings.expand_bookings("db.json"),ROOM_COUNT)
    calendar = calendar_builder.add_html_class_by_date(calendar, unavailable, "unavailable")
    past = bookings.collect_past_dates()
    calendar = calendar_builder.add_html_class_by_date(calendar, past, "past")

    return flask.render_template("index.html", booking=booking, calendar=calendar, unavailable=unavailable)


if __name__ == "__main__":
    app.run(debug=True)
