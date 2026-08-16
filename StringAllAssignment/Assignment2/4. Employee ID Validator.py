'''4.
Employee ID Validator
A company wants to validate employee IDs before storing them in the database.
Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID

'''

emid=input("Enter Employee ID : ")

fir=emid[0].upper()
sec=emid[1].upper()
third=emid[2].upper()
digit=0
if len(emid)==8:
    if fir=='E' and sec=='M' and third=='P':
        for ch in range(3,len(emid)):
            if emid[ch].isdigit():
                digit=digit+1
            else:
                print("Remaining characters should be digits only")
                break
        if digit==len(emid)-3:
            print("Valid Employee ID ")

    else:
        print("Employe id start with EMP ")
    

else:
    print("Length should be 8 of Employe ID ")

