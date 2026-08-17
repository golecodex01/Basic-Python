allowed=frozenset("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
username=""

while True:
    print("1. Enter Username")
    print("2. Validate Username")
    print("3. Display Allowed Characters")
    print("4. Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        username=input("Enter Username: ")

    elif choice==2:
        valid=True

        for ch in username:
            if ch not in allowed:
                valid=False
                break

        if valid:
            print("Valid Username")
        else:
            print("Invalid Username")

    elif choice==3:
        print(allowed)

    elif choice==4:
        break

    else:
        print("Invalid Choice")