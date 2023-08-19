"""main file running webapp"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import BookingForm
from calendar_frame import generate_calendar

SEE_MONTHS_IN_ADVANCE = 12


app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"
Bootstrap(app)


@app.route('/', methods=["GET", "POST"])
def index():
    booking = BookingForm()
    calendar = generate_calendar(SEE_MONTHS_IN_ADVANCE)
    # Old code from new_booking when it was a script. Use in booking form.
    # email = input("email?: ")
    # date = input("first night?(yyyymmdd): ")
    # dur = int(input("how many nights?: "))
    # new_booking = {date: {"room06": [email, dur]}}
    return render_template("index.html", booking=booking, calendar=calendar)


if __name__ == "__main__":
    app.run(debug=True)
