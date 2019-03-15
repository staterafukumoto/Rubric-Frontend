from flask import Flask, render_template, request, redirect, url_for
import sqlite3

#TODO...
#Add request if statement to student function. 
#Add try/Catch statement to student name enter.
#Remove Student function
#Add CSS and clean up code
#Make /user not look... gross.
#Score button? - Half done
#Does not take names with a space - try/catch
#Consider switching to MYSQL
#Switch /students to the Index page
#User handling
#More than one classes
#Automatic redirect on UserRoute?
#Reset student score button - Push
#Can't have more than 4 or less than 0


#Initializes SQL Dsatabase
conn = sqlite3.connect("twoDadDatabase.db")
print("Opened database sucsessfully")
conn.close()

app = Flask(__name__)       


@app.route('/', methods = ['POST', 'GET'])
def students():

    students = request.form.getlist('name[]')

    with sqlite3.connect("twoDadDatabase.db") as con:
        cur = con.cursor()

        for i in range(len(students)):
            cur.execute("INSERT INTO students(name) VALUES (? )", (students[i],))

        con.commit()
        print("Value Inserted")

    cur.execute("SELECT name from students LIMIT 20")
    studentsDB = cur.fetchall()

    
    return render_template("students.html", students = studentsDB)

@app.route('/remove', methods = ['POST', 'GET'])
def remove():
    pass    

    return render_template('remove.html')

@app.route('/removeResult', methods = ['POST'])
def removeResult():
    name = request.form['name']

    with sqlite3.connect("twoDadDatabase.db") as con:
        cur = con.cursor()    

        cur.execute("DELETE FROM students WHERE name =?", (name,))
        con.commit()

    return render_template('removeResult.html')

@app.route('/result', methods = ['POST'])
def results():
    numberOfStudents = int(request.form["num"])

    return render_template("results.html", num=numberOfStudents)



@app.route('/students', methods = ['POST', 'GET'] )
def add():
    return render_template("index.html")



@app.route('/user', methods = ['POST'])
def user():

    studentSQL = request.form['StudentDB']

    with sqlite3.connect("twoDadDatabase.db") as con:
        cur = con.cursor()

        cur.execute("SELECT * FROM students WHERE name =? ", (studentSQL,))
        dataTest = cur.fetchall()


    return render_template("user.html", student=studentSQL, data=dataTest)



@app.route('/userRoute', methods= ['POST'])
def userRoute():

    studentSQL = request.form['submit']

    with sqlite3.connect("twoDadDatabase.db") as con:
        cur = con.cursor()
        
        def addValue():

            #Preparedness
            if request.form.get("minusOne1", False):
                cur.execute("UPDATE students SET Preparedness = Preparedness - 1 WHERE name =? ", (studentSQL,)) 
                print("-1 on Preparedness for " + studentSQL)
            elif request.form.get("plusOne1", False):
                cur.execute("UPDATE students SET Preparedness = Preparedness + 1 WHERE name =? ", (studentSQL,))
                print("+1 on Preparedness for " + studentSQL)
            else:
                print("No value for Preparedness")

            #Engagement
            if request.form.get("minusOne2", False):
                cur.execute("UPDATE students SET Engagement = Engagement - 1 WHERE name =? ", (studentSQL,)) 
                print("-1 on Preparedness for " + studentSQL)
            elif request.form.get("plusOne2", False):
                cur.execute("UPDATE students SET Engagement = Engagement + 1 WHERE name =? ", (studentSQL,))
                print("+1 on Preparedness for " + studentSQL)
            else:
                print("No value for Engagement")        

            #Perseverance
            if request.form.get("minusOne3", False):
                cur.execute("UPDATE students SET Perseverance = Perseverance - 1 WHERE name =? ", (studentSQL,)) 
                print("-1 on Preparedness for " + studentSQL)
            elif request.form.get("plusOne3", False):
                cur.execute("UPDATE students SET Perseverance = Perseverance + 1 WHERE name =? ", (studentSQL,))
                print("+1 on Preparedness for " + studentSQL)
            else:
                print("No value for Perseverance") 

            #Problem Solving
            if request.form.get("minusOne4", False):
                cur.execute("UPDATE students SET ProblemSolving = ProblemSolving - 1 WHERE name =? ", (studentSQL,)) 
                print("-1 on Preparedness for " + studentSQL)
            elif request.form.get("plusOne4", False):
                cur.execute("UPDATE students SET ProblemSolving = ProblemSolving + 1 WHERE name =? ", (studentSQL,))
                print("+1 on Preparedness for " + studentSQL)
            else:
                print("No value for ProblemSolving")        

            #Professionalism
            if request.form.get("minusOne5", False):
                cur.execute("UPDATE students SET Professionalism = Professionalism - 1 WHERE name =? ", (studentSQL,)) 
                print("-1 on Preparedness for " + studentSQL)
            elif request.form.get("plusOne5", False):
                cur.execute("UPDATE students SET Professionalism = Professionalism + 1 WHERE name =? ", (studentSQL,))
                print("+1 on Preparedness for " + studentSQL)
            else:
                print("No value for Professionalism")  
        addValue()

        #Score script
        cur.execute("SELECT Preparedness, Engagement, Perseverance, ProblemSolving, Professionalism FROM students WHERE name =? ", (studentSQL,))
        score = cur.fetchall()
        # More than 4
        for x in score:
            scoreFinal = int(x[0]) + int(x[1]) + int(x[2]) + int(x[3]) + int(x[4])
            print(str(scoreFinal) + " out of 20 or " + str(scoreFinal * 5) + "%")
            scorePercent = scoreFinal * 5

    return render_template("userRoute.html", student=studentSQL, score=scoreFinal, scoreP = scorePercent)


if __name__ == "__main__":
    app.run(debug=True)