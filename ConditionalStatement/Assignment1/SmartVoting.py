age=int(input("Enter Your Age :" ))
id=input("Do you have ID proof(YES / NO) :" )
id=id.lower()

if age>=22:
     print("Eligible to Vote ")
     if id=="yes":
        print("Allowed Inside the Booth ")
     else:
        print("Do Not have any Id Proof")
else :
     print("Under Age ")