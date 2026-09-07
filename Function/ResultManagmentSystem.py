'''
      
Constraints

* Marks should be between 0 and 100.
* Display an appropriate message for invalid marks.
* The program should continue until the user chooses Exit.

Sample Input / Output

******** STUDENT RESULT MANAGEMENT ********

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Result
6. Find Highest Mark
7. Find Lowest Mark
8. Exit

Enter Choice : 1

Enter Student Name : Ajay
Enter Roll Number : 101

Enter Mark 1 : 78
Enter Mark 2 : 85
Enter Mark 3 : 92
Enter Mark 4 : 88
Enter Mark 5 : 77

Student details added successfully.

Enter Choice : 2

Total Marks = 420

Enter Choice : 3

Percentage = 84.0

Enter Choice : 4

Grade = A

Enter Choice : 6

Highest Mark = 92

Enter Choice : 7

Lowest Mark = 77

Enter Choice : 5

----------- RESULT CARD -----------

Name        : Ajay
Roll Number : 101

Marks
Subject 1 : 78
Subject 2 : 85
Subject 3 : 92
Subject 4 : 88
Subject 5 : 77

Total Marks : 420
Percentage  : 84.0
Grade       : A
Highest Mark: 92
Lowest Mark : 77

Enter Choice : 8

Thank You. Program Terminated.

Important Instructions

1. The solution must be developed using multiple user-defined functions.
2. Use appropriate parameters wherever data needs to be passed between functions.
3. Use return statements wherever a function needs to send a result back to the caller.
4. Avoid using unnecessary global variables.
5. Implement the application using a menu-driven approach.
6. Perform proper input validation.
7. Write meaningful function names and maintain proper code readability.

Functional Requirements


'''
def add_studentdetails(marks):
    name=input("Enter Student Name : ")
    rollnum=input("Enter Roll Number : ")
    marks=[]
    for i in range(5):
        print("Enter marks of ",i+1,"Subject : ")
        marks.append(i)

def calculate_totalmarks(marks):
    sum=sum(marks)
    return sum

def calculate_percentage(total):
    percent=total/5
    return percent

def find_grade(percent):
    
        if percent >=90:
            print("A+ ")
        elif percent >=80:
            print("A ")
        elif percent >=70:
            print("B ")
        elif percent >=60:
            print("C ")
        elif percent >=50:
            print("D ")
        else:
             print("Fail ")




def lowest_marks(marks):
     return min(marks)

def highest_marks(marks):
     return max(marks)
     


def display_result(name,rollnum,grade,total,percent,highest_marks,lowest_marks,marks):
     print("----------- RESULT CARD -----------")
     print("Name : ",name)
     print("Roll Number : ",rollnum)
     print("Marks ")
     for i in range(5):
          print("Subject ",i+1," : ",marks[i])
          print("Total Marks : ",total)
          print("Percentage : ",percent)
          print("Grade : ",grade)
          print("Highest Marks : ",highest_marks)
          print("Lowest Marks : ",lowest_marks)     




    

    

marks=[]

while True:

print(" ******** STUDENT RESULT MANAGEMENT ******** ")
print("1. Add Student Details ")
print("2. Calculate Total Marks ")
print("3. Calculate Percentage  ")
print("4. Find Grade ")
print("5. Display Result ")
print("6. Find Highest Marks ")
print("7. Find Lowest Marks ")
print("8. Exit ")

n=int(input("Enter your Choice : "))
match n:
    case 1:
        add_studentdetails()
    case 2:
        calculate_totalmarks(marks)
    case 3:
        calculate_percentage()
    case 4:
        find_grade()
    case 5:
        display_result()
    case 6:
        highest_marks()
    case 7:
        lowest_marks()
    case 8:
        print("Thank You ! Program Terminates SuccessFully ")
        break
    case _:
        print("Please enter a valid number ")

      










