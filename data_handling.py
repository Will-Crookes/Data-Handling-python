def displayMenu():
    print("1. Input data and overwrite existing entries (Warning: This will erase all previous entries!")
    print("2. Input data and append to existing file")
    print("3. Calculate and display average mark")
    print("4. Display data")
    print("5. Quit")
    choice = input("Please enter your chosen number")
    if choice == "1":
        option1()
    elif choice == "2":
        option2()
    elif choice == "3":
        option3()
    elif choice == "4":
        option4()
    elif choice == "5":
        exit()
    else:
        print("Please enter a valid option of 1-5")
        displayMenu()
    return
def option1():
    testResultsFile = open("studentNamesfile.txt", "w")
    resultsfile = open("resultsfile.py", "w")
    totalentries = open("totalEntries.py", "w")
    studentMark = "0"
    studentName = input("Enter a students name, (type xxx to exit option): ")
    if studentName != "xxx":
        studentMark = input("Enter mark: ")
        testResultsFile.write(studentName)
        testResultsFile.write(" ")
        testResultsFile.write("%s\n" % studentMark)
        resultsfile.write("total_score = ")
        resultsfile.write(studentMark)
        totalentries.write("total = 1")
        testResultsFile.close()
        resultsfile.close()
        totalentries.close()
        option2()           #runs option2 so that new name entries don't keep running over the previous
    else:
        displayMenu()

def option2():
    testResultsFile = open("studentNamesfile.txt", "a")
    resultsfile = open("resultsfile.py", "a")
    totalentries = open("totalEntries.py", "a")
    studentMark = "0"
    studentName = input("Enter a students name, (type xxx to exit option): ")
    if studentName != "xxx":
        studentMark = input("Enter mark: ")
        testResultsFile.write(studentName)
        testResultsFile.write(" ")
        testResultsFile.write("%s\n" % studentMark)
        resultsfile.write(" + ")
        totalentries.write(" + 1")
        resultsfile.write(studentMark)
        testResultsFile.close()
        resultsfile.close()
        totalentries.close()
        option2()
    else:
        displayMenu()
    return

def option3():
    from resultsfile import total_score
    from totalEntries import total
    average = total_score / total
    print(average, "\n\n")
    displayMenu()

def option4():
    testResultsFile= open("studentNamesfile.txt", 'r')
    for line in testResultsFile:
        words = line.split()
        print(words)
    displayMenu()


displayMenu()
