#TODO...
#General Bugfixes
#Be able to pick more students, not just a set amount.
#Update score function to show all sections score. -DONE
#Have teacher pick a number of students, then ramdomly pick x amount of students to check on.


#Student Picked must be defined here because it is not used by rubricValueInput
student = ''
anotherStudent = ''
studentPicked = ''

numberOfStudents = 4

rubric = ["Preparedness", "Engagement", "Perseverance", "Problem solving", "Professionalism"]

rublicDictionary = {"Preparedness": 3, "Engagement": 3, "Perseverance": 3, "Problem Solving": 3, "Professionalism": 3}

goodBadList = ["good", "bad"]

threeValueList = ["value", "score", "exit"]

def pickStudent():
    #We need to define student picked as global so it will transfer over to the CompileScore function.
    global studentPicked
    studentPicked = ''
    print('\nPlease select your student...')
    print("\n".join(student_list))
    # While Loop is used to make sure that until a proper student is picked, it will take user input.
    while studentPicked not in student_list:
        studentPicked = input().capitalize()

    if studentPicked == student_list[0]:
        print("You picked... " + student_list[0])
        rubricValueInput()

    elif studentPicked == student_list[1]:
        print("You picked... " + student_list[1])
        rubricValueInput()

    elif studentPicked == student_list[2]:
        print("You picked... " + student_list[2])
        rubricValueInput()

    elif studentPicked == student_list[3]:
        print("You picked... " + student_list[3])
        rubricValueInput()

    else:
        print("Error... Line186")

def threeValue():
    yesNo = input().lower()
    if yesNo == 'value':
        rubricValueInput()
    elif yesNo == 'score':
        CompileScore()
    elif yesNo == 'exit':
        exit()
    else:
        print("Please enter a valid command")
        threeValue()

def CompileScore():
    #We need to bring the variable in here AS GLOBAL or it will not work.
    global studentPicked
    # Preparedness
    if rublicDictionary['Preparedness'] >= 4:
        rublicDictionary['Preparedness'] = 4
    if rublicDictionary['Preparedness'] <= 1:
        rublicDictionary['Preparedness'] = 1

    # Engagement
    if rublicDictionary['Engagement'] >= 4:
        rublicDictionary['Engagement'] = 4
    if rublicDictionary['Engagement'] <= 1:
        rublicDictionary['Engagement'] = 1

    # Perseverance
    if rublicDictionary['Perseverance'] >= 4:
        rublicDictionary['Perseverance'] = 4
    if rublicDictionary['Perseverance'] <= 1:
        rublicDictionary['Perseverance'] = 1

    # Problem Solving
    if rublicDictionary['Problem Solving'] >= 4:
        rublicDictionary['Problem Solving'] = 4
    if rublicDictionary['Problem Solving'] <= 1:
        rublicDictionary['Problem Solving'] = 1

    # Professionalism
    if rublicDictionary['Professionalism'] >= 4:
        rublicDictionary['Professionalism'] = 4
    if rublicDictionary['Professionalism'] <= 1:
        rublicDictionary['Professionalism'] = 1

    finalScore = rublicDictionary['Preparedness'] + rublicDictionary['Engagement'] + rublicDictionary['Perseverance'] + rublicDictionary['Problem Solving'] + rublicDictionary['Professionalism']
    print('Final score for ' + studentPicked + ' is ' + str(finalScore) + ' out of 20' + ' or ' + str(finalScore * 5) + '%') # the % sign is not used for formatting, it is latterly just used as a %
    print('Preparedness ' + str(rublicDictionary['Preparedness']))
    print('Engagement ' + str(rublicDictionary['Engagement']))
    print('Perseverance ' + str(rublicDictionary['Perseverance']))
    print('Problem Solving' + str(rublicDictionary['Problem Solving']))
    print('Professionalism ' + str(rublicDictionary['Professionalism']))

    print('Would you like to grade another student?')
    anotherStudent = input().lower()
    if anotherStudent == 'yes':
        rublicDictionary['\nPreparedness'] = 3
        rublicDictionary['Engagement'] = 3
        rublicDictionary['Perseverance'] = 3
        rublicDictionary['Problem Solving'] = 3
        rublicDictionary['Professionalism\n'] = 3
        pickStudent()
    else:
        exit()

def rubricValueInput():
    #RubrickSection and goodBad MUST be defined here, it will not read outside of this function.
    rubricSection = ''
    goodBad = ''
    print("\nPlease select the section of the Rubric. \n")
    print("\n".join(rubric))
    while rubricSection not in rubric:
        rubricSection = input().capitalize()

        if rubricSection == rubric[0]:
            print("You picked... " + rubric[0])
            print("Good or Bad Feedback...")

            while goodBad not in goodBadList:
                goodBad = input().lower()

                if goodBad == goodBadList[0]:
                    rublicDictionary['Preparedness'] += 1
                    print(rublicDictionary['Preparedness'])
                    print("Would you like to enter another value, Score, or Exit?")
                    print("value, score, exit")
                    threeValue()

                if goodBad == goodBadList[1]:
                    rublicDictionary['Preparedness'] -= 1
                    print(rublicDictionary['Preparedness'])
                    print("Would you like to enter another value, Score, or Exit?")
                    print("value, score, exit")
                    threeValue()

        if rubricSection == rubric[1]:
            print("You picked... " + rubric[1])
            print("Good or Bad Feedback...")

            while goodBad not in goodBadList:
                goodBad = input().lower()

                if goodBad == goodBadList[0]:
                    rublicDictionary['Engagement'] += 1
                    print(rublicDictionary['Engagement'])
                    print("Would you like to enter another value, Score, or Exit?")
                    print("value, score, exit")
                    threeValue()

                if goodBad == goodBadList[1]:
                    rublicDictionary['Engagement'] -= 1
                    print(rublicDictionary['Engagement'])
                    print("Would you like to enter another value, Score, or Exit?")
                    print("value, score, exit")
                    threeValue()

        if rubricSection == rubric[2]:
            print("You picked... " + rubric[2])
            print("Good or Bad Feedback...")

            while goodBad not in goodBadList:
                goodBad = input().lower()

                if goodBad == goodBadList[0]:
                    rublicDictionary['Engagement'] += 1
                    print(rublicDictionary['Engagement'])
                    print("Would you like to enter another value, Score, or Exit?")
                    print("value, score, exit")
                    threeValue()

                if goodBad == goodBadList[1]:
                    rublicDictionary['Engagement'] -= 1
                    print(rublicDictionary['Engagement'])
                    print("Would you like to enter another value, Score, or Exit?")
                    print("value, score, exit")
                    threeValue()

        if rubricSection == rubric[3]:
            print("You picked... " + rubric[3])
            print("Good or Bad Feedback...")

            while goodBad not in goodBadList:
                goodBad = input().lower()

                if goodBad == goodBadList[0]:
                    rublicDictionary['Problem Solving'] += 1
                    print(rublicDictionary['Problem Solving'])
                    print("Would you like to enter another value, Score, or Exit?")
                    print("value, score, exit")
                    threeValue()

                if goodBad == goodBadList[1]:
                    rublicDictionary['Problem Solving'] -= 1
                    print(rublicDictionary['Problem Solving'])
                    print("Would you like to enter another value, Score, or Exit?")
                    print("value, score, exit")
                    threeValue()

        if rubricSection == rubric[4]:
            print("You picked... " + rubric[4])
            print("Good or Bad Feedback...")

            while goodBad not in goodBadList:
                goodBad = input().lower()

                if goodBad == goodBadList[0]:
                    rublicDictionary['Professionalism'] += 1
                    print(rublicDictionary['Professionalism'])
                    print("Would you like to enter another value, Score, or Exit?")
                    print("value, score, exit")
                    threeValue()

            if goodBad == goodBadList[1]:
                rublicDictionary['Professionalism'] -= 1
                print(rublicDictionary['Professionalism'])
                print("Would you like to enter another value, Score, or Exit?")
                print("value, score, exit")
                threeValue()

# Start of actual output code
number_of_students = int(input("Enter number of students: "))
student_list = []

#loops for the number of times you pick first, then input the names into a list using append.
for i in range(number_of_students):
    student = input("Enter name: ").capitalize()
    student_list.append(student)

pickStudent()
