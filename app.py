import pickle
import json
import requests
from flask import Flask, render_template, request 
#from app.user.routes import *


app = Flask(__name__)
app.static_folder = "static"

netflix = {"name": "Netflix", "day": 1.7, "month": 51, "cost":  "$12.99", "url": "netflix"}
nyt = {"name": "New York Times", "day": 0.2, "month": 2, "cost":  "$17.99", "url": "nyt"}
prime = {"name": "Amazon Prime", "day": 0.1, "month": 1, "cost":  "$7.99", "url": "prime"}
spotify = {"name": "Spotify", "day": 5, "month": 150, "cost":  "$5.99", "url": "spotify"}
goog = {"name": "Google One", "day": 0, "month": 0.5, "cost":  "$2.99", "url": "google"}

lst = [netflix, nyt, prime, spotify, goog]


@app.route("/")
def index(): 
    return render_template("home.html")

@app.route("/signin")
def login(): 
    return render_template("login.html")

@app.route("/newSubscription")
def new(): 
    return render_template("new.html")

@app.route("/login", methods=["POST"])
def validate():
    print(request.form.keys())
    print(request.form.get("inputPassword"))
    if (request.form.get("inputEmail") == "Team10@AmpHacks.com" and
        request.form.get("inputPassword") == "AMPHACKSROX"): 
        return render_template("dashboard.html", lst=lst)
    else:
        render_template("signin.html")
        #To Do: Send back error message

@app.route("/addNew", methods=["POST"])
def addNew():
    new = {"name": request.form.get("name"), "day": "n/a",
    "month": request.form.get("usage"), "cost": "$" + request.form.get("cost"), "url":
    request.form.get("name").replace(" ", "")}
    lst.append(new)
    return render_template("dashboard.html", lst=lst)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", lst=lst, 
    message="You almost never use Google One, consider unsubcribing?")

# # reads in the ML model
# try:
#     with open("./model_pickle", 'rb') as file:
#         predictionModel = pickle.load(file)
# except IOError as e:
#         print(e)

@app.route("/signout")
def signOut():
    return render_template("home.html")

@app.route("/netflix")
def netflix():
    return render_template("netflix.html")

# Makes a prediction with the ML model and formats a json message based on 
# prediction results
def makePrediction(data, subscriber):
    result = predictionModel.predict([data])

    if result[0] == 0:
        message = {
            "Subscriber" : subscriber,
            "Prediction" : "almost never",
            "Message" : "You almost never use "+ subscriber +" consider unsubcribing?"
        }

    elif result[0] == 1:
        message = {
            "Subscriber" : subscriber,
            "Prediction" : "rarely",
            "Message" : "You rarely " +subscriber+" save some money?"
        }
    
    elif result[0] == 2:
        message = {
            "Subscriber" : subscriber,
            "Prediction" : "almost never",
            "Message" : ""
        }
    
    elif result[0] == 3:
        message = {
            "Subscriber" : subscriber,
            "Prediction" : "very often",
            "Message" : ""
        }
    
    return json.dumps(message)

# calls make prediction with arbitrary values to generate a json message
def generateMessage(data, subscriber):
    # hardcoded arbitrary values
    data = [
        0.2918,
        2.042440929,
        8.753318267,
        26.2599548
    ]

    jsonMessage = makePrediction(data, "Audible")

    #send out the json message
    try:
        r = requests.post("https://localhost:8000", json=jsonMessage)
    except Exception as e:
        print(e)

#generateMessage(None, None)

if __name__ == '__main__':
    app.run(use_reloader=True) 