from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, DateField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired

class DataInput(FlaskForm):
    brand = SelectField("Brand", choices=[("audi", "Audi"), ("bmw", "BMW"), ("ford", "Ford"), ("hyundai", "Hyundai"), ("Mercedes", "Mercedes"), ("skoda", "Skoda"), ("toyota", "Toyota"), ("vauxhall", "Vauxhall"), ("vw", "VW")], validators=[DataRequired()])
    model = StringField("Model", validators=[DataRequired()])
    engine = DecimalField("Engine size", validators=[DataRequired()])
    y = DecimalField("Year", validators=[DataRequired()])
    km = DecimalField("km driven", validators=[DataRequired()])
    gear = RadioField("Gearbox type", choices=[("manuel", "Manuel"), ("automatic", "Automatic")], validators=[DataRequired()])
    fuel = RadioField("Fuel type", choices=[("petrol" ,"Petrol"), ("diesel", "Diesel")], validators=[DataRequired()])
    fe = DecimalField("Fuel economy", validators=[DataRequired()])
    submit = SubmitField("Submit")
