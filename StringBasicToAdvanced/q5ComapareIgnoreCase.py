s1=input("Enter your First String : ")
s2=input("Enter your Second String : ")
flag=True

if len(s1)!=len(s2):
    flag =False
else:
    for i in range(len(s1)):
        if s1[i].lower()!=s2[i].lower():
            flag=False
            break

if flag:
    print("Equal ")
else:
    print("Not Equal ")