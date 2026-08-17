isbn=set()

while True:
    print("1. Add ISBN")
    print("2. Remove ISBN")
    print("3. Search ISBN")
    print("4. Display ISBN List")
    print("5. Count Books")
    print("6. Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        number=input("Enter ISBN: ")
        isbn.add(number)

    elif choice==2:
        number=input("Enter ISBN: ")
        if number in isbn:
            isbn.remove(number)
        else:
            print("ISBN not found")

    elif choice==3:
        number=input("Enter ISBN: ")
        if number in isbn:
            print("ISBN Found")
        else:
            print("ISBN Not Found")

    elif choice==4:
        print(isbn)

    elif choice==5:
        print(len(isbn))

    elif choice==6:
        break

    else:
        print("Invalid Choice")