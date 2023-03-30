"""
Shreyaas Sureshbabu
Assignment 9
Problem 3
"""

course_id = input("Enter a course ID (i.e. CS0002, CS0004): ") #asks user for a class name

def open_file_classdata(): #opens the class_data file
    user_file = open("class_data.txt", "r")
    return user_file

def open_file_roster(): #opens the enrollment_data file
    user_file = open("enrollment_data.txt", "r")
    return user_file

def course_splitter(): #splits the class data file into two lists of equal length: one with ID name, one with the class' actual name
    x = open_file_classdata()
    x = x.read()
    x = x.replace("\n", ",")
    classes = x.split(",")
    class_id = []
    class_name = []
    for i in range(len(classes)):
        if i % 2 == 0:
            class_id += [classes[i]]
        elif i % 2 == 1:
            class_name += [classes[i]]
    return [class_id, class_name]

def roster_splitter(): #splits the enrollment_data file into individual elements (ex. [id, first name, last name])
    y = open_file_roster()
    y = y.read()
    y = y.replace("\n", ",")
    students = y.split(",")
    return students

def course_name(course_id): #finds the course name if it exists and prints it, otherwise returns False for later 
    x = course_splitter()
    class_id = x[0]
    class_name = x[1]
    try:
        for i in range(len(class_id)):
            if course_id in class_id[i]:
                print("The title of this class is: " + str(class_name[i]))
                selected_course = class_id[i]
        return selected_course
    except:
        print("Cannot find this course.")
        return False
        
def students_enrolled(): #finds the number of students enrolled and stores their name into a list
    y = roster_splitter()
    total = 0
    student_names = []
    for i in range(0, len(y), 3):
        if course_id == y[i]:
            total += 1
            name = y[i + 1] + "," + y[i + 2]
            student_names += [name]
        else:
            continue
    return [total, student_names]

def main(): #runs the code
    y = course_name(course_id)
    x = students_enrolled()
    total = x[0]
    names = x[1]
    if y == False:
        return 0
    else:
        print("The course has " + str(total) + " students enrolled")
        for i in range(total):
            print("* " + names[i])

main()



