PassWord=input("Enter Your Password :")
space=0
digit=0
lower=0
upper=0
special=0
for ch in PassWord:
    if ch.isupper():
        upper=1
    elif ch.islower():
        lower=1
    elif ch.isdigit():
        digit=1
    elif ch.isspace():
        space=1
    else:
        special=1

if len(PassWord)>=8 and len(PassWord)<=15:
    elif upper==1 and lower==1 and digit==1 and space==1 and special==1:
        print("Valid Password ")

else:
    print("Invalid Password ")