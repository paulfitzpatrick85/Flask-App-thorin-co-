import os
# import Flask from flask. capital f Flask is class name
# saves from having to type html with tags etc
import json
from flask import Flask, render_template 

app = Flask(__name__)    


# app.route decorator
# tell flask what url should trigger function that follows,/ goes to top file
@app.route("/")    
def index():
    return render_template("index.html")  # will render html page 


@app.route("/about")
def about():                                                      # pyhton list
    data = []
    # python opens json file as read only and asigns data to json_data
    with open("data/company.json", "r") as json_data:
        # set empty data list to equal parsed json data thats sent through
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data) 
# company is a new variable, it is sent to html template,
# its equal to list of data from json file


#  <> pass data from url path to the view 
@app.route("/about/<member_name>")
def about_member(member_name):  # view(can take the above as arg)
    member = {}  # empty obj to store data later
    with open("data/company.json", "r") as json_data:  # open as read-only call it json_data
        data = json.load(json_data)  # convert data pulled thru into json + store in data
        for obj in data:  # iterate thru data
            if obj["url"] == member_name:
                member = obj  # empty obj member be = to obj in loop instance
    return render_template("member.html", member=member)  # 1st member is variable passed thru to html file, 2nd is from line 32 + 37


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")  # the view*


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")

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