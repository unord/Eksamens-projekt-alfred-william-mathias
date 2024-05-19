from flask import render_template, redirect, session, url_for
from app import app
from app.forms import DataInput
import pickle as pkl
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd

preprocessor = pkl.load(open("preprocessor.pkl", "rb"))
model = pkl.load(open("model.pkl", "rb"))

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    form = DataInput()
    pred_price = None
    if form.validate_on_submit():
        pred_data = {col: [data] for col, data in zip(form.data.keys(), [data if isinstance(data, str) else float(data) for data in form.data.values()])}
        pred_data = pd.DataFrame(pred_data)
        pred_data = preprocessor.transform(pred_data)
        pred_price = abs(round(model.predict(pred_data)[0]))
        redirect("/")
    return render_template("index.html", title="Used car pricepicker", form=form, price=pred_price)
