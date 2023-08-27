"""main file running webapp"""
import flask
from flask_bootstrap import Bootstrap
from forms import BookingForm
import calendar_builder
import bookings


SEE_MONTHS_IN_ADVANCE = 12
ROOM_COUNT = 4


app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"
Bootstrap(app)


@app.route('/', methods=["GET", "POST"])
def index():
    booking = BookingForm()
    calendar = calendar_builder.generate_calendar(SEE_MONTHS_IN_ADVANCE)
    unavailable = bookings.room_availability(bookings.expand_bookings("db.json"),ROOM_COUNT)
    calendar = calendar_builder.add_html_class_by_date(calendar, unavailable, "unavailable")
    # Old code from new_booking when it was a script. Use in booking form.
    # email = input("email?: ")
    # date = input("first night?(yyyymmdd): ")
    # dur = int(input("how many nights?: "))
    # new_booking = {date: {"room06": [email, dur]}}
    return flask.render_template("index.html", booking=booking, calendar=calendar)


if __name__ == "__main__":
    app.run(debug=True)
