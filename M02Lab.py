# Charles W.
# M02Lab - Case Study
# Will take 5 students names and GPA's to see if they qualify for the Dean's List/Honor Role and provide feedback accordingly

numStudents = 0

while numStudents != 5:

    studentName = str(input('Please enter student name: '))

    if studentName == 'ZZZ' or studentName == 'zzz':
        break

    studentGPA = float(input('Please enter student GPA: '))

    if studentGPA >= 3.5:
        print(studentName + " has made the Dean's List")

    elif studentGPA >=3.25 and studentGPA < 3.5:
        print(studentName + " has made the honor role")

    else:
        print("Thank you for trying your best.. here is a cookie:)")

    print()
    numStudents += 1