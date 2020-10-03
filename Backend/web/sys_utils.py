
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt # for hashing the password

client = MongoClient("mongodb://db:27017") # connecting mkongodb to our database db at the default port

db = client.SimilarityDB
users = db["users"] # our collection users

# helper functions 
"""
    Checks whether a user already exists in the database 
       
    Parameters:
        username: the unique identification name for the user <str>
    Returns:
        True/False <boolean>
"""
def userExists(username):
    if users.find({"username": username}).count() == 0:
        return False
    else:
        return True

"""
    Verifies password provided by the user against the one already present in the database
       
    Parameters:
        username: the unique identification name for the user <str>
        password : password given at the time of calling the API <str>
    Returns:
        True/False <boolean>
"""
def verifypw(username, password):
    hashed_pw = users.find({
        "username" : username
    })[0]["password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False