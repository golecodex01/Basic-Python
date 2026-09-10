msg=input("Enter your String : ")

ch=input("Enter your Character : ")

for i in range(len(msg)):
    if msg[i]==ch:
        print("Character found at index ",i)
        break
else:
    print("Element not Found ")
    