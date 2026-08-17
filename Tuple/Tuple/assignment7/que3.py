visitors=set()

while True:
    print("1. Add Visitor")
    print("2. Remove Visitor")
    print("3. Check Visitor")
    print("4. Display All Visitors")
    print("5. Count Unique Visitors")
    print("6. Clear Visitor Data")
    print("7. Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        visitor=input("Enter Visitor ID: ")
        visitors.add(visitor)

    elif choice==2:
        visitor=input("Enter Visitor ID: ")
        if visitor in visitors:
            visitors.remove(visitor)
        else:
            print("Visitor not found")

    elif choice==3:
        visitor=input("Enter Visitor ID: ")
        if visitor in visitors:
            print("Visitor Found")
        else:
            print("Visitor Not Found")

    elif choice==4:
        print(visitors)

    elif choice==5:
        print(len(visitors))

    elif choice==6:
        visitors.clear()
        print("Visitor Data Cleared")

    elif choice==7:
        break

    else:
        print("Invalid Choice")