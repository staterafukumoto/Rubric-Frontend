from flask import Flask, render_template, request, redirect, url_for
import sqlite3

#TODO today
#More than one class - Done!
#Update SQL function to inclue the new system of sorting- Done!
#Look into DISTINCT in SQLite3 - Done!
#Remove number of students add function, I don't like it - Done
#Add more titles - Done!
#fix the /student post requests - Fixed
#Create class in webApp - Done!
#Clean Templates Folder - Done

#TODO in the future
#Ask sid to scetch out how he wants his frontend to look - Sid, Beta 0.2
#Add CSS / margins - Sid, Beta 0.2
#I hate the score list on /user - Sid, Beta 0.2
#Remoeve Function with new SQL method - Beta 0.2
#Remove function general update - Beta 0.2
#Reset student score button - Beta 0.25
#Consider switching to MYSQL - Beta 0.3
#Consider switching to Django - Beta 0.3
#Random select student function - Beta 0.4
#User handling - Beta 0.5
#Does not take names with a space - try/catch -Push 
#Add try/Catch statement to student name enter. - Push 
#Check removed - Push

'''Use functions to declare vars, so you only declare the var when you actaully need it
Example, def test1(): request.getform['testvar']    if x == y: test1()''' 
# ^ This actually works!


#Initializes SQL Dsatabase
conn = sqlite3.connect("twoDadDatabase.db")
print("Opened Database Sucsessfully")
conn.close()

app = Flask(__name__)       

@app.route('/', methods = ['POST', 'GET'])
def classes():

    with sqlite3.connect("twoDadDatabase.db") as con:
            cur = con.cursor()

            cur.execute("SELECT DISTINCT ClassName from students")
            classSelected = cur.fetchall()    

    return render_template("class.html", Class = classSelected)



@app.route('/studentList', methods = ['POST'])
def students():
    studentClass = request.form['Class']
        
    with sqlite3.connect("twoDadDatabase.db") as con:
        cur = con.cursor()

        cur.execute("SELECT name FROM students WHERE className =?", (studentClass,))
        studentsDB = cur.fetchall()

        
    return render_template("index.html", students = studentsDB, studentClass = studentClass)



@app.route('/student', methods = ['POST'])
def user():

    studentSQL = request.form['StudentDB']

    with sqlite3.connect("twoDadDatabase.db") as con:
        cur = con.cursor()

        cur.execute("SELECT * FROM students WHERE name =? ", (studentSQL,))
        dataTest = cur.fetchall()


    return render_template("user.html", student=studentSQL, data=dataTest)



@app.route('/student/Route', methods= ['POST'])
def userRoute():

    studentSQL = request.form['submit']

    with sqlite3.connect("twoDadDatabase.db") as con:
        cur = con.cursor()
        
        def addValue():

            #Preparedness
            if request.form.get("button1", False):
                button1 = request.form["button1"]
                if button1 == "-1":
                    cur.execute("UPDATE students SET Preparedness = Preparedness - 1 WHERE name =? ", (studentSQL,)) 
                    print("-1 on Preparedness for " + studentSQL)
                elif button1 == "+1":
                    cur.execute("UPDATE students SET Preparedness = Preparedness + 1 WHERE name =? ", (studentSQL,))
                    print("+1 on Preparedness for " + studentSQL)
            else:
                print("No value for Preparedness")

            #Engagement
            if request.form.get("button2", False):
                button2 = request.form["button2"]
                if button2 == "-1":
                    cur.execute("UPDATE students SET Engagement = Engagement - 1 WHERE name =? ", (studentSQL,)) 
                    print("-1 on Engagement for " + studentSQL)
                elif button2 == "+1":
                    cur.execute("UPDATE students SET Engagement = Engagement + 1 WHERE name =? ", (studentSQL,))
                    print("+1 on Engagement for " + studentSQL)
            else:
                print("No value for Engagement")

            #Perseverance
            if request.form.get("button3", False):
                button3 = request.form["button3"]
                if button3 == "-1":
                    cur.execute("UPDATE students SET Perseverance = Perseverance - 1 WHERE name =? ", (studentSQL,)) 
                    print("-1 on Perseverance for " + studentSQL)
                elif button3 == "+1":
                    cur.execute("UPDATE students SET Perseverance = Perseverance + 1 WHERE name =? ", (studentSQL,))
                    print("+1 on Perseverance for " + studentSQL)
            else:
                print("No value for Perseverance")

            #Problem Solving
            if request.form.get("button4", False):
                button4 = request.form["button4"]
                if button4 == "-1":
                    cur.execute("UPDATE students SET ProblemSolving = ProblemSolving - 1 WHERE name =? ", (studentSQL,)) 
                    print("-1 on Problem Solving for " + studentSQL)
                elif button4 == "+1":
                    cur.execute("UPDATE students SET ProblemSolving = ProblemSolving + 1 WHERE name =? ", (studentSQL,))
                    print("+1 on Problem Solving for " + studentSQL)
                else:
                    print("No value for ProblemSolving")  
            else:
                print("No value for Problem Solving")

            #Professionalism 
            if request.form.get("button5", False):
                button5 = request.form["button5"]
                if button5 == "-1":
                    cur.execute("UPDATE students SET Professionalism = Professionalism - 1 WHERE name =? ", (studentSQL,)) 
                    print("-1 on Professionalism for " + studentSQL)
                elif button5 == "+1":
                    cur.execute("UPDATE students SET Professionalism = Professionalism + 1 WHERE name =? ", (studentSQL,))
                    print("+1 on Professionalism for " + studentSQL)
                else:
                    print("No value for Professionalism") 
            else:
                print("No value for Professionalism")        

        addValue()

        #Score script
        cur.execute("SELECT Preparedness, Engagement, Perseverance, ProblemSolving, Professionalism FROM students WHERE name =? ", (studentSQL,))
        score = cur.fetchall()
        # More than 4
        for x in score:
            num1 = x[0]
            num2 = x[1]
            num3 = x[2]
            num4 = x[3]
            num5 = x[4]

            #Num1
            if num1 >= 4:
                num1 = 4
            elif num1 <= 0:
                num1 = 0

            #num2
            if num2 >= 4:
                num2 = 4
            elif num2 <= 0:
                num2 = 0
            
            #Num3
            if num3 >= 4:
                num3 = 4
            elif num3 <= 0:
                num3 = 0

            #num4
            if num4 >= 4:
                num4 = 4
            elif num4 <= 0:
                num4 = 0

            #num5
            if num5 >= 4:
                num5 = 4
            elif num5 <= 0:
                num5 = 0

            scoreFinal = num1 + num2 + num3 + num4 + num5
            print(str(scoreFinal) + " out of 20 or " + str(scoreFinal * 5) + "%")
            scorePercent = scoreFinal * 5

    return render_template("userRoute.html", student=studentSQL, score=scoreFinal, scoreP = scorePercent)



@app.route('/remove', methods = ['GET'])
def remove():

    return render_template('remove.html')



@app.route('/remove/result', methods = ['POST'])
def removeResult():
    name = request.form['name']

    with sqlite3.connect("twoDadDatabase.db") as con:
        cur = con.cursor()    

        cur.execute("DELETE FROM students WHERE name =?", (name,))
        con.commit()

    return render_template('removeResult.html', student=name)



@app.route('/add', methods = ['GET'])
def add():
    with sqlite3.connect("twoDadDatabase.db") as con:
            cur = con.cursor()

            cur.execute("SELECT DISTINCT ClassName from students")
            classSelected = cur.fetchall()        

    return render_template("add.html", Class = classSelected)



@app.route('/add/result', methods = ['POST'])
def addStudent():
    Class = request.form['Class']
    Name = request.form['name']
    with sqlite3.connect("twoDadDatabase.db") as con:
        cur = con.cursor()

        cur.execute("INSERT INTO students(name, ClassName) VALUES (?, ? )", (Name, Class,))
        con.commit()
        print("Student(s) added")

    return render_template("AddResults.html", Class = Class, Name = Name)



@app.route('/addClass', methods = ['POST'])
def addClass():

    return render_template ("addClass.html")



@app.route('/addClass/student', methods = ['POST'])
def addClassStudent():
    Class = request.form['className']
    Name = request.form['name']

    with sqlite3.connect("twoDadDatabase.db") as con:
        cur = con.cursor()

        cur.execute("INSERT INTO students(name, ClassName) VALUES (?, ?)", (Name, Class, ))

    return render_template("addClassStudent.html", Class = Class, Name = Name)



if __name__ == "__main__":
    app.run(debug=True)