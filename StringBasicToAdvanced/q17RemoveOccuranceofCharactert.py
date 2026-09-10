msg=input("ENter your Messsage : ")
ch=input("Enter your CHaracter : ")
result=""
for i in msg:
    if i!=ch:
        result=result+i

print(result)