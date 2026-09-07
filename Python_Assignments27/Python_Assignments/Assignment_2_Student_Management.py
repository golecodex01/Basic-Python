students = {
    101: {
        "name": "Ajay",
        "course": "Python",
        "mobile": "9876543210",
        "fees": 25000,
        "city": "Indore"
    },
    102: {
        "name": "Ravi",
        "course": "Java",
        "mobile": "9876500000",
        "fees": 22000,
        "city": "Bhopal"
    }
}

while True:
    print("\n=========================================")
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=========================================")
    print("1. Add New Student")
    print("2. Search Student")
    print("3. Update Course")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Count Total Students")
    print("7. Display Students By Course")
    print("8. Display Students By City")
    print("9. Find Student Paying Highest Fees")
    print("10. Find Student Paying Lowest Fees")
    print("11. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        student_id = int(input("Enter Student ID: "))

        if student_id in students:
            print("Student ID Already Exists")
        else:
            name = input("Enter Student Name: ")
            course = input("Enter Course Name: ")
            mobile = input("Enter Mobile Number: ")
            fees = int(input("Enter Fees: "))
            city = input("Enter City: ")

            students[student_id] = {
                "name": name,
                "course": course,
                "mobile": mobile,
                "fees": fees,
                "city": city
            }

            print("Student Added Successfully")

    elif choice == 2:
        student_id = int(input("Enter Student ID: "))

        if student_id in students:
            print("\nStudent ID :", student_id)
            print("Name       :", students[student_id]["name"])
            print("Course     :", students[student_id]["course"])
            print("Mobile     :", students[student_id]["mobile"])
            print("Fees       :", students[student_id]["fees"])
            print("City       :", students[student_id]["city"])
        else:
            print("Student Not Found")

    elif choice == 3:
        student_id = int(input("Enter Student ID: "))

        if student_id in students:
            new_course = input("Enter New Course: ")
            students[student_id]["course"] = new_course
            print("Course Updated Successfully")
        else:
            print("Student Not Found")

    elif choice == 4:
        student_id = int(input("Enter Student ID: "))

        if student_id in students:
            del students[student_id]
            print("Student Deleted Successfully")
        else:
            print("Student Not Found")

    elif choice == 5:
        if len(students) == 0:
            print("No Students Found")
        else:
            for student_id, data in students.items():
                print("\n-----------------------------------")
                print("Student ID :", student_id)
                print("Name       :", data["name"])
                print("Course     :", data["course"])
                print("Mobile     :", data["mobile"])
                print("Fees       :", data["fees"])
                print("City       :", data["city"])
                print("-----------------------------------")

    elif choice == 6:
        print("Total Students :", len(students))

    elif choice == 7:
        course = input("Enter Course : ")
        found = False

        for student_id, data in students.items():
            if data["course"].lower() == course.lower():
                print(student_id, data["name"])
                found = True

        if found == False:
            print("No Students Found")

    elif choice == 8:
        city = input("Enter City : ")
        found = False

        for student_id, data in students.items():
            if data["city"].lower() == city.lower():
                print(student_id, data["name"])
                found = True

        if found == False:
            print("No Students Found")

    elif choice == 9:
        if len(students) == 0:
            print("No Students Found")
        else:
            highest_id = max(students, key=lambda id: students[id]["fees"])

            print("\nHighest Fee Paying Student")
            print("Student ID :", highest_id)
            print("Name       :", students[highest_id]["name"])
            print("Course     :", students[highest_id]["course"])
            print("Fees       :", students[highest_id]["fees"])

    elif choice == 10:
        if len(students) == 0:
            print("No Students Found")
        else:
            lowest_id = min(students, key=lambda id: students[id]["fees"])

            print("\nLowest Fee Paying Student")
            print("Student ID :", lowest_id)
            print("Name       :", students[lowest_id]["name"])
            print("Course     :", students[lowest_id]["course"])
            print("Fees       :", students[lowest_id]["fees"])

    elif choice == 11:
        print("\nThank You For Using Student Management System")
        break

    else:
        print("Invalid Choice! Please try again.")
