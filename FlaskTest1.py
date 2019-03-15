from flask import Flask, render_template, request, redirect, url_for
import sqlite3

#TODO...
#Add request if statement to student function. -Done! (in a way)
#Make /user not look... gross. -WIP
#Score button? - Will make the value hide, but not show...
#I hate the score list on /user


#Ask sid to scetch out how he wants his frontend to look
#Add CSS and clean up code  - Ongoing 
#Switch /students to the Index page -Done
#More than one classes 
#Automatic redirect on UserRoute
#Can't have more than 4 or less than 0 
#User handling 
#Consider switching to MYSQL
#Not required to select a catagory   
#Can select all buttons, cannot de-select - Fixed
#Does not take names with a space - try/catch -Push
#Add try/Catch statement to student name enter. - Push
#Reset student score button - Push

#Use functions to declare vars, so you only declare the var when you actaully need it
#Example, def test1(): request.getform['testvar']    if x == y: test1()


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



@app.route('/remove', methods = ['GET'])
def remove():

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



@app.route('/students', methods = ['GET'] )
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
            button1 = request.form["button1"]
            button2 = request.form["button2"]
            button3 = request.form["button3"]
            button4 = request.form["button4"]
            button5 = request.form["button5"] 

            if button1 == "-1":
                cur.execute("UPDATE students SET Preparedness = Preparedness - 1 WHERE name =? ", (studentSQL,)) 
                print("-1 on Preparedness for " + studentSQL)
            elif button1 == "+1":
                cur.execute("UPDATE students SET Preparedness = Preparedness + 1 WHERE name =? ", (studentSQL,))
                print("+1 on Preparedness for " + studentSQL)
            else:
                print("No value for Preparedness")

            #Engagement
            if button2 == "-1":
                cur.execute("UPDATE students SET Engagement = Engagement - 1 WHERE name =? ", (studentSQL,)) 
                print("-1 on Preparedness for " + studentSQL)
            elif button2 == "+1":
                cur.execute("UPDATE students SET Engagement = Engagement + 1 WHERE name =? ", (studentSQL,))
                print("+1 on Preparedness for " + studentSQL)
            else:
                print("No value for Engagement")        

            #Perseverance
            if button3 == "-1":
                cur.execute("UPDATE students SET Perseverance = Perseverance - 1 WHERE name =? ", (studentSQL,)) 
                print("-1 on Preparedness for " + studentSQL)
            elif button3 == "+1":
                cur.execute("UPDATE students SET Perseverance = Perseverance + 1 WHERE name =? ", (studentSQL,))
                print("+1 on Preparedness for " + studentSQL)
            else:
                print("No value for Perseverance") 

            #Problem Solving
            if button4 == "-1":
                cur.execute("UPDATE students SET ProblemSolving = ProblemSolving - 1 WHERE name =? ", (studentSQL,)) 
                print("-1 on Preparedness for " + studentSQL)
            elif button4 == "+1":
                cur.execute("UPDATE students SET ProblemSolving = ProblemSolving + 1 WHERE name =? ", (studentSQL,))
                print("+1 on Preparedness for " + studentSQL)
            else:
                print("No value for ProblemSolving")        

            #Professionalism
            if button5 == "-1":
                cur.execute("UPDATE students SET Professionalism = Professionalism - 1 WHERE name =? ", (studentSQL,)) 
                print("-1 on Preparedness for " + studentSQL)
            elif button5 == "+1":
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