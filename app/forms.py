from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, DateField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired

class DataInput(FlaskForm):
    model = StringField("Model", validators=[DataRequired()])
    year = DecimalField("Year", validators=[DataRequired()])
    transmission = RadioField("Transmission", choices=[("Manual", "Manual"), ("Automatic", "Automatic")], validators=[DataRequired()])
    mileage = DecimalField("Mileage", validators=[DataRequired()])
    fuelType = RadioField("Fuel type", choices=[("Petrol" ,"Petrol"), ("Diesel", "Diesel")], validators=[DataRequired()])
    mpg = DecimalField("MPG (miles per gallon)", validators=[DataRequired()])
    engineSize = DecimalField("Engine size", validators=[DataRequired()])
    brand = SelectField("Brand", choices=[("audi", "Audi"), ("bmw", "BMW"), ("ford", "Ford"), ("hyundai", "Hyundai"), ("Mercedes", "Mercedes"), ("skoda", "Skoda"), ("toyota", "Toyota"), ("vauxhall", "Vauxhall"), ("vw", "VW")], validators=[DataRequired()])
    submit = SubmitField("Submit")
