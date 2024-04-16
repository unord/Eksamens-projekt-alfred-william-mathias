from flask import render_template, redirect, session, url_for
from app import app
from app.forms import DataInput

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    form = DataInput()
    data = ""
    if form.validate_on_submit():
        data = {
            "brand": form.brand.data,
            "model": form.model.data,
            "engine": form.engine.data,
            "year": form.y.data,
            "km": form.km.data,
            "gear": form.gear.data,
            "fuel": form.fuel.data,
            "fe": form.fe.data
        }
        redirect("/")
    return render_template("index.html", title="Used car pricepicker", form=form, data=data)
