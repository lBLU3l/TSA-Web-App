from flask import Flask, redirect, url_for, render_template, request
import calFuncs

# Calling all calendar functions

month = calFuncs.findMonth()
year = calFuncs.findYear()
date = calFuncs.findDate()
day = calFuncs.findDay()
hour = calFuncs.findHour()
greet = calFuncs.timeGreet()

app = Flask(__name__)        # SETS VAR AS THE APPLICATION



@app.route("/") # THIS IS THE BASIC HOME PAGE WITH NO EXTRA ARGS, EX. (GOOGLE.COM/)
def home(): # WHAT HAPPENS WHEN WE VISIT THE HOME PAGE
    return render_template("demo.html", greet = greet) # INDEX.HTML CONTROLS WHAT IS SHOWN ON SCREEN

@app.route("/<usr>") # SET USR TO ARG, EX. IF URL = (GOOGLE.COM/JOHN), USR = JOHN
def user(usr): # WHAT HAPPENS WHEN USER FUNCTION OPENED UP
    return f"<h1>Could not find page: {usr}</h1>" # DISPLAY THE USER'S NAME

@app.route("/spreadsheet")
def spreadsheet():
    return "this is the spreadsheet page"

@app.route("/to-do")
def todo():
    return render_template("to-do.html", date = date, day = day, month = month)

@app.route("/calendar")
def calendar():
    return render_template("calendar.html", month = " ".join(month.upper()), year = " ".join(year), day = day, date = date)
    

@app.route("/notepad")
def notepad():
    return "this is the notepad page"

if __name__ == "__main__":
    app.run(debug=True)

