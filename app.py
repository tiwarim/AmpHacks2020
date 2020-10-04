import pickle
import json
import requests

# reads in the ML model
try:
    with open("./model_pickle", 'rb') as file:
        predictionModel = pickle.load(file)
except IOError as e:
        print(e)

# Makes a prediction with the ML model and formats a json message based on 
# prediction results
def makePrediction(data, subscriber):
    result = predictionModel.predict([data])

    if result[0] == 0:
        message = {
            "Subscriber" : subscriber,
            "Prediction" : "almost never",
            "Message" : f"You almost never use {subscriber}, consider unsubcribing?"
        }

    elif result[0] == 1:
        message = {
            "Subscriber" : subscriber,
            "Prediction" : "rarely",
            "Message" : f"You rarely {subscriber}, save some money?"
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
        r = requests.post("https://localhost:8080", json=jsonMessage)
    except Exception as e:
        print(e)

generateMessage(None, None)