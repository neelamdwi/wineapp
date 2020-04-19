from application import app
from flask import render_template, request, json, jsonify
import requests

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/wineregress", methods=['GET', 'POST'])
def wineregress():

    #extract form inputs
    fixed_acidity = request.form.get("fixed_acidity")
    volatile_acidity = request.form.get("volatile_acidity")
    citric_acid = request.form.get("citric_acid")
    residual_sugar = request.form.get("residual_sugar")
    chlorides = request.form.get("chlorides")
    free_sulfur_dioxide = request.form.get("free_sulfur_dioxide")
    total_sulfur_dioxide = request.form.get("total_sulfur_dioxide")
    density = request.form.get("density")
    pH = request.form.get("pH")
    sulphates = request.form.get("sulphates")
    alcohol = request.form.get("alcohol")

    #url for wineratingservice
    url = "https://wineratingservice-app.herokuapp.com/api"

    #create json from form inputs
    data = json.dumps({"fixed_acidity": fixed_acidity, "volatile_acidity": volatile_acidity, "citric_acid": citric_acid, "residual_sugar": residual_sugar, "chlorides": chlorides, "free_sulfur_dioxide": free_sulfur_dioxide, "total_sulfur_dioxide": total_sulfur_dioxide, "density": density, "pH": pH, "sulphates": sulphates, "alcohol": alcohol })

    #post json to url
    results =  requests.post(url,data)

    #send prediction result to index.html for display
    return render_template("index.html", results=results.content.decode('UTF-8'))
  
