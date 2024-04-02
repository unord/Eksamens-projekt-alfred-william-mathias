from flask import render_template, redirect
from app import app
from app.forms import DataInput

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    form = DataInput()
    data_entered = False
    if form.validate_on_submit():
        data_entered = True
        return redirect("/index")
    return render_template("index.html", title="Daytrading minmaxxer", form=form, data_entered=data_entered)
