alphabets=set("abcdefghijklmnopqrstuvwxyz")
sentence=""

while True:
    print("1. Enter Sentence")
    print("2. Display Missing Alphabets")
    print("3. Count Missing Alphabets")
    print("4. Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        sentence=input("Enter Sentence: ")
        sentence=sentence.lower()

    elif choice==2:
        present=set(sentence)
        missing=alphabets.difference(present)
        print(missing)

    elif choice==3:
        present=set(sentence)
        missing=alphabets.difference(present)
        print(len(missing))

    elif choice==4:
        break

    else:
        print("Invalid Choice")