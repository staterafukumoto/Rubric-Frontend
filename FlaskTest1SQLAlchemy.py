from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

#TODO...
#test.html, need to find a way to allow multiple forms with only ONE submit button. - Done! (Thank god)
#user.html need to make students a list instead of one var, currently it's only printing the first name.
#Add some git you lazy fatass.
#Add request if statement to student function. 
#Learn how to import functions from another script.

#define list length in the script call 

#We don't actally acsess the SQL, we get the data, output it all based off witch user you are, then have you select based off of the choice from ALL Data.

#Initializes SQL Database
app = Flask(__name__)  # NOT SQL 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/C:/Users/wallingr/Desktop/Auto-Grading-Rubric-new-master/twoDadDatabase.db'


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/result', methods = ['POST'])
def results():
    numberOfStudents = int(request.form["num"])

    return render_template("results.html", num=numberOfStudents)



@app.route('/students', methods = ['POST', 'GET'] )
def students():
    students = request.form.getlist('name[]')

    return render_template("students.html", studentNum = len(students), students = students)



@app.route('/user', methods = ['POST'])
def user():
    return render_template("user.html")



if __name__ == "__main__":
    app.run(debug=True) #We need Debug on because we are developing it, console will display more information.%A