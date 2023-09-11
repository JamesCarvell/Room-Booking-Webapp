"""main file running webapp"""
import datetime

from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap

from forms import BookingForm
import calendar_builder
import bookings


SEE_MONTHS_IN_ADVANCE = 12
ROOM_COUNT = 4


app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"
Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def index():
    form = BookingForm()
    unavailable = bookings.check_room_availability(bookings.expand_bookings("db.json"),ROOM_COUNT)

    if form.validate_on_submit():
        start_date_string = form.start_date.data
        start_date = datetime.date.fromisoformat(start_date_string)
        if (start_date <= (datetime.date.today() - datetime.timedelta(days=1))):
            flash("Your booking started in the past, and failed.")
            return redirect(url_for("index"))
        end_date_string = form.end_date.data
        end_date = datetime.date.fromisoformat(end_date_string)

        for month_and_year, day_list in unavailable.items():
            for day_temp in day_list:
                tentative_date = datetime.datetime.strptime(month_and_year + " " + str(day_temp), "%B %Y %d").date()
                if (start_date <= tentative_date) and (tentative_date <= end_date):
                    flash("Your booking contained an unavailable date, and failed.")
                    return redirect(url_for("index"))
            
        email = form.email.data
        duration_timedelta = end_date - start_date
        duration_int = int(duration_timedelta.total_seconds() / (60 * 60 * 24)) + 1
        new_booking = {"room04": {start_date_string: [email, duration_int]}}
        bookings.create_new_booking("db.json", new_booking)
        flash("Your booking was successful!")
        return redirect(url_for("index"))

    calendar = calendar_builder.generate_calendar(SEE_MONTHS_IN_ADVANCE)
    calendar = calendar_builder.add_html_class_by_date(calendar, unavailable, "unavailable")
    past = bookings.collect_past_dates()
    calendar = calendar_builder.add_html_class_by_date(calendar, past, "past")
    return render_template("index.html", form=form, calendar=calendar, unavailable=unavailable)


if __name__ == "__main__":
    app.run(debug=True)
