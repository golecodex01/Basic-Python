s1=input("Enter s1 ")
s2=input("ENter s2 ")
s1count=0
s2count=0
if len(s1)!=len(s2):
    print("Not Ana")
else:
    for i in s1 :
        s1count=s1count+ord(i)
    for j in s2:
        s2count=s2count+ord(j)
    if s1count==s2count:
        print("Annaaa")

    else:
        print("Not annaaa ")  
          