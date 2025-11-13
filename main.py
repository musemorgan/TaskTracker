# This will serve as the main coding elements for my personal task tracker project

# Importing the FastAPI class from fastapi module, look into what module is?
from fastapi import FastAPI 

app = FastAPI() 
# 5 defines my new app that im creating
# app is an object, it is where interaction between the client and browser take place
# fast api is a webframework, something that helps to simplify api creation [look to see if webframework is just a specialized api?]

# defining a path
@app.get("/")
def read_root():
        return {"Message": "Congrats! This is your first API"}
# def root & return a function ? look more into this
# lines 10 is a route decorator, defines http location that will serve as the endpoint [in this case get-message]
# what is placed above works in the terminal and postman, is the sole purpose of postman for checking?