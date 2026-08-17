coding=set()
robotics=set()

while True:
    print("1. Add Student to Coding Club")
    print("2. Add Student to Robotics Club")
    print("3. Display Students in Coding Club")
    print("4. Display Students in Robotics Club")
    print("5. Find Students in Both Clubs")
    print("6. Find Students Only in Coding Club")
    print("7. Find Students Only in Robotics Club")
    print("8. Display All Unique Club Members")
    print("9. Display Total Unique Club Members")
    print("10. Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        student=input("Enter Student ID: ")
        coding.add(student)

    elif choice==2:
        student=input("Enter Student ID: ")
        robotics.add(student)

    elif choice==3:
        print(coding)

    elif choice==4:
        print(robotics)

    elif choice==5:
        print(coding.intersection(robotics))

    elif choice==6:
        print(coding.difference(robotics))

    elif choice==7:
        print(robotics.difference(coding))

    elif choice==8:
        print(coding.union(robotics))

    elif choice==9:
        print(len(coding.union(robotics)))

    elif choice==10:
        break

    else:
        print("Invalid Choice")