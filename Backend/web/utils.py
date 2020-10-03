# importing libraries
from sys_utils import *

# Resource Register
"""
    Resource Register takes input on a POST protocol and creates new accounts 
    Parameters:
        namepass: contains username and password of the user <JSON>
    Returns:
        retJson: contains status code and message <JSON>
"""
class Register(Resource):
    def post(self):
        namepass = request.get_json()
        username = namepass["username"]
        password = namepass["password"]

        # check if the user already exists
        if userExists(username):
            retJson = {
                "statuscode" : 301,
                "message" : "User Already exists"
            }
            return jsonify(retJson)

        hashedpw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        users.insert({
            "username" : username,
            "password" : hashedpw,
            "tokens" : 6
        })
        retJson = {
            "statuscode" : 200,
            "message" : "you successfuly signed up for the api"
        }
        return jsonify(retJson)