import os
# import Flask from flask. capital f Flask is class name
# saves from having to type html with tags etc
from flask import Flask, render_template    

app = Flask(__name__)    


# app.route decorator
@app.route("/")    # flask what url should trigger function that follows
def index():
    return render_template("index.html")  # will render html page 


# create instancce of class. convention in flask is that variable is called app
# first arg of flask class is the name of the apps module/package
# single module used so __name__ is used = built in python variable, 
# flask needs it to look for templates and static files

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True  # only for test, SET TO FALSE FOR PROJECT!!!!
    )