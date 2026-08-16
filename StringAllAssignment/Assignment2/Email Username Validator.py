'''1.
Email Username Validator
A company wants to check whether an employee email username is valid before creating an official account.
Conditions:

- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters
Input:
Enter username: ajay_123
Output:
Valid Username
'''
user=input("Enter UserName : ")
first=user[0].upper()

if len(user)>=5 and len(user)<=12:
    
    if first>='A' and first<='Z':
        for ch in user:
            if ch ==" ":
                print("Space is Not Allowed ")
                break
        else:
            print("Valid UserName  : ",user)
    else:
        print("PLease Enter 1st Character Alphabet ")


else:
    print("Please Enter Username in range between 5 to 12 letters ")