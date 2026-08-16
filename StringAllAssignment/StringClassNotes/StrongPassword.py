pw=input("Enter Password : ")
l=len(pw)
uppercase=0
lowercase=0
digit=0
space=0
special=0

for ch in pw:
    if ch>='A' and ch<='Z':
        uppercase=1
    elif ch>='a' and ch<='z':
        lowercase=1
    elif ch>='0' and ch<='9':
        digit=1
    elif ch==' ':
        space=1
    else:
        special=1
    

if l>8 and l<15 and uppercase==1 and lowercase==1 and space==0 and digit==1 and special==1:
    print("Valid Password ")

else:
     print("Invalid PassWord ")