from sys_utils import *
from utils import *

app = Flask(__name__)
api = Api(app) # initialize that this app would be an api

# assigning a route to the resources 
api.add_resource(Register, "/register")
# api.add_resource(Start, "/start")
# api.add_resource(Dashboard, "/dashboard")



if __name__ == "__main__":
    app.run(host="0.0.0.0")