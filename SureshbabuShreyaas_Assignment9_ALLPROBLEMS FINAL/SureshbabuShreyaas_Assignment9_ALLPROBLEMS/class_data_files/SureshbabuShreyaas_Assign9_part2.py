"""
Shreyaas Sureshbabu
Assignment 9
Problem 2
"""

filename = input("Enter a class file to grade (i.e class1 for class1.txt): ") #asks user for a file name
def file_exists(filename): #makes sure file exists
    try:
        filepath = filename + ".txt"
        user_file = open(filepath, "r")
        return user_file
    except:
        print("File cannot be found.")
        return False

#part 2b
def grade_exam(): #grades a class' exams 
    try:
        x = file_exists(filename)
        grades = x.read()
        class_grades = grades.split("\n")
        answerkey = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
        answers = answerkey.split(",")
        unused = 0
        j = 0
        scores = []
        for i in range(len(class_grades)): #after splitting the list up into individual strings, makes temporary list to split each of those strings into their own lists and grading them
            score = 0
            z = 0
            grds = [] #temp list for each student ID and their answers
            grds = class_grades[i].split(",")
            if len(grds) != 26: #if length of list is not 26, line is unusable
                unused += 1
                class_grades[i] = []
                continue
            else: #grades students' answers and adds it to a list
                for j in range(1, len(grds)):
                    if grds[j] in answers[z]:
                        if grds[j] == "":
                            score += 0
                            z += 1
                        else:
                            score += 4
                            z += 1
                    elif grds[j] not in answers[z]:
                        score -= 1
                        z += 1
                scores += [score]
        return [scores, unused, len(class_grades)]
    except:
        print("Cannot be graded since file does not exist.")

def sort_list(): #helper function to sort the grades by ascending order
    x = grade_exam()
    score = x[0]
    score.sort()
    return score

def median(): #finds median by taking necessary indexes of sorted list
    x = sort_list()
    i = len(x)
    if i % 2 == 0:
        lower = (i//2) - 1
        higher = (i//2) 
        median = (x[higher] + x[lower])/2
        med = format(median, '.2f')
    if i % 2 == 1:
        scores = x.sort()
        med_val = (i//2) + 1
        median = x[med_val]
        med = format(median, '.2f')
    return median

def mode(): #finds mode by looking through each value and finding maximum occurrences
    x = sort_list()
    total = 0
    minimum = min(x)
    maximum = max(x)
    list = [0] * ((maximum - minimum) + 1)
    for i in range(len(x)):
        list[x[i] - minimum] += 1

    list_max = max(list)
    mode = ""

    for i in range(len(list)):
        if list[i] == list_max:
            mode += str(i + minimum) + " "    
    
    return mode

def range_num(): #finds range by taking difference between max and min
    x = sort_list()
    minimum = min(x)
    maximum = max(x)
    range = maximum - minimum
    return range
   
def grade_summary(): #summarizes a class' grades through the necessary given information
    try:
        x = grade_exam()
        scores = x[0]
        unused = x[1]
        class_grades = x[2]

        f = class_grades - unused

        min_max = scores.sort()
        max = scores[-1]
        min = scores[0]

        avg = 0
        for i in range(len(scores)):
            avg += scores[i]
        average = avg/f
        av = format(average, '.2f')

        med = median()

        mo = mode()

        ra = range_num()
        if file_exists(filename) != False:
            print("Successfully opened " + filename + ".txt")
        print("Grade summary:")
        print("Total students:", f)
        print("Unused lines:", unused)
        print("Highest score:", max)
        print("Lowest score:", min)
        print("Mean score: " + av)
        print("Median score:", med)
        print("Mode:", mo)
        print("Range:", ra)
    except:
        print("File cannot have a grade summary since file does not exist.")

def report_grades(): #gives a report of a classes grades in given format
    try:
        if file_exists(filename) != False:
            filepath = filename + "_results.txt"
            user_file = open(filepath, "a")
            x = file_exists(filename)
            grades = x.read()
            class_grades = grades.split("\n")
            id_num = []
            i = 0
            while i < len(class_grades):
                grds = []
                grds = class_grades[i].split(",")
                if len(grds) != 26:
                    class_grades.remove(class_grades[i])
                    i -= 1
                i += 1
            for i in range(len(class_grades)):
                id_num.append(class_grades[i][0:9])
            y = grade_exam()
            list_y = y[0]
            for i in range(len(list_y)):
                list_y[i] = float(list_y[i])
            for i in range(len(id_num)):
                data = id_num[i] + "," + format(list_y[i], '.2f') + "\n"
                user_file.write(data)
    except:
        print("Report cannot be generated.")

def main(): #main function to run everything 
    grade_summary()
    report_grades()

main()
