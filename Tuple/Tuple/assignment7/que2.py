python=set()
java=set()

while True:
    print("1. Enroll Student in Python")
    print("2. Enroll Student in Java")
    print("3. Display Python Students")
    print("4. Display Java Students")
    print("5. Find Students Enrolled in Both Courses")
    print("6. Find Students Enrolled Only in Python")
    print("7. Find Students Enrolled Only in Java")
    print("8. Check Enrollment in Python Course")
    print("9. Display Total Unique Students")
    print("10. Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        email=input("Enter Email: ")
        python.add(email)

    elif choice==2:
        email=input("Enter Email: ")
        java.add(email)

    elif choice==3:
        print(python)

    elif choice==4:
        print(java)

    elif choice==5:
        print(python.intersection(java))

    elif choice==6:
        print(python.difference(java))

    elif choice==7:
        print(java.difference(python))

    elif choice==8:
        email=input("Enter Email: ")
        if email in python:
            print("Student is enrolled in Python")
        else:
            print("Student is not enrolled in Python")

    elif choice==9:
        print(len(python.union(java)))

    elif choice==10:
        break

    else:
        print("Invalid Choice")