msg=input("Enter your String : ")

result=""
space=False

for i in msg:

    if i != ' ':
        result=result+i
        space=False

    elif result != "" and space == False:
        result=result+' '
        space=True

print("Modified String :",result)

msg=input("ENter your String : ")
result=""
space=False



