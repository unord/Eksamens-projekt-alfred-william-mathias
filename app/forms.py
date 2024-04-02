from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, DateField, SubmitField
from wtforms.validators import DataRequired

class DataInput(FlaskForm):
    name = StringField("stock name", validators=[DataRequired()])
    price = DecimalField("current price", validators=[DataRequired()])
    date = DateField("Current date", validators=[DataRequired()])
    submit = SubmitField("Submit")
