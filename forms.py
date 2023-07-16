from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class BookingForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    date = StringField("Date", validators=[DataRequired()])
    duration = StringField("# of Night", validators=[DataRequired()])
    submit = SubmitField("Book Me!")
