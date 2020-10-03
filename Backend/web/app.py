app = Flask(__name__)
api = Api(app) # initialize that this app would be an api

# assigning a route to the resources 
api.add_resource(Register, "/register")
api.add_resource(Refill, "/start")
api.add_resource(Detect, "/dashboard")



if __name__ == "__main__":
    app.run(host="0.0.0.0")