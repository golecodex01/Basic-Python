s1=""
s2=""

while True:
    print("1. Enter First String")
    print("2. Enter Second String")
    print("3. Display Common Characters")
    print("4. Count Common Characters")
    print("5. Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        s1=input("Enter First String: ")

    elif choice==2:
        s2=input("Enter Second String: ")

    elif choice==3:
        a=set(s1)
        b=set(s2)
        common=a.intersection(b)
        print(common)

    elif choice==4:
        a=set(s1)
        b=set(s2)
        common=a.intersection(b)
        print(len(common))

    elif choice==5:
        break

    else:
        print("Invalid Choice")