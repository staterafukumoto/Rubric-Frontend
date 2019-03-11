from flask import Flask, render_template, request, redirect, url_for
import os.path
import sqlite3

#TODO...
#test.html, need to find a way to allow multiple forms with only ONE submit button. - Done! (Thank god)
#user.html need to make students a list instead of one var, currently it's only printing the first name. - Done!
#Add some git you lazy fatass.
#Add request if statement to student function. 
#Testing my GIT

#Initializes SQL Database
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

    return render_template("students.html", studentNum = len(students), students = students)



@app.route('/user', methods = ['POST'])
def user():
    return render_template("user.html")



if __name__ == "__main__":
    app.run(debug=True) #We need Debug on because we are developing it, console will display more information.%A