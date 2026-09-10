msg=input("Enter  your Message : ")
old=input("Enter yourr old character to replace ")
new=input("Enter new character to replace old one ")
result=""
for i in msg:
    if i==old:
        result=result+new
    else:
        result+=i

print(result)