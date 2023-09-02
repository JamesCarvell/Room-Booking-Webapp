from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class BookingForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    start_date = StringField("Start Date", validators=[DataRequired()])
    end_date = StringField("End Date", validators=[DataRequired()])
    submit = SubmitField("Book Me!")
