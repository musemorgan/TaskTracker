#This will serve as the main coding elements for my personal task tracker project

#Importing the API
from fastapi import FastAPI # similar to SQL, but not sure of significance
app = FastAPI() #defines my new app that im creating
#app is an object, it is where interaction between the client and browser take place

#defining a path
@app.get("/")# lines 9-10 is an app decorator, defines http location so it will take us to whatever route place in here
def root():
        return {"Hello World"}
#def root & return a function ? look more into this