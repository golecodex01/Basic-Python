msg=input("Enter your String : ")
result=""
for i in msg:
    if i>='a' and i<='z':
        ch=chr(ord(i)-32)
        result=result+ch
    else:
        result=result+i
print("Modified String : ",result)

