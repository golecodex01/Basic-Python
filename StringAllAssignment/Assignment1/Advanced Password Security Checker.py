'''Advanced Password Security Checker
A cyber security company wants to verify whether employee passwords are highly secure before giving system access.
Conditions: Password must:
Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters
Input: Enter password: Python@45
Output: Secure Password



Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters
Input: Enter password: Python@45
Output: Secure Password
'''

pw=input("Enter Password : ")
first=pw[0]

if len(pw)>=8 and len(pw)<=15:
    if first>='A' and first<='Z':
        last=pw[-1]
        if  last.isdigit():
            if 
            
        


        else:
            print("Please Enter last character must be digit ")
    

    else:
        print("PLease Enter FIrst Letter Must be Capital ")



else:
    print("Please Enter Password in given range between 8 to 15 letters ")    
