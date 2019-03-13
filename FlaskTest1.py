from flask import Flask, render_template, request, redirect, url_for
import os.path
import sqlite3

#TODO...
#Add some git you lazy fatass. - Done :/
#Add request if statement to student function. 
#Add try/Catch statement to student name enter.
#Can't get past Students
#Pass student var from Database into next site page. (Hard?)
#Does not take names with a space :/

#Look into Node.JS to acsess the SQLite database, we don't NEED to edit the SQL in Python.
#Consider switching to MYSQL

#Initializes SQL Dsatabase
conn = sqlite3.connect("twoDadDatabase.db")
print("Opened database sucsessfully")
conn.close()

app = Flask(__name__)       

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

    with sqlite3.connect("twoDadDatabase.db") as con:
        cur = con.cursor()

        for i in range(len(students)):
            cur.execute("INSERT INTO students(name) VALUES (? )", (students[i],))

        con.commit()
        print("Value Recorded")
    
    cur.execute("SELECT name from students LIMIT 20")
    studentsDB = cur.fetchall()


    return render_template("students.html", students = studentsDB)



@app.route('/user', methods = ['POST'])
def user():
    studentSQL = request.form["StudentDB"]


    return render_template("user.html", student=studentSQL)


@app.route('/userRoute', methods = ['POST'])
def userRoute():

    studentSQL2 = request.form["value"]

    with sqlite3.connect("twoDadDatabase.db") as con:
        cur = con.cursor()

        cur.execute("SELECT * FROM students WHERE name =? ", (studentSQL2,))
        dataTest = cur.fetchall()
    
        if request.form.get("minusOne", False):
            cur.execute("UPDATE students SET Preparedness = Preparedness - 1 WHERE name =? ", (studentSQL2,))
            print("-1 on Preparedness for " + studentSQL2)
        if request.form.get("plusOne", False):
            print("Maybe Flask ins't that bad...")



    return render_template("test.html", student=studentSQL2, data=dataTest)



if __name__ == "__main__":
    app.run(debug=True)