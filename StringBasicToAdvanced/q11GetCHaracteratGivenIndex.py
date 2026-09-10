msg=input("Enter your String : ")
end=len(msg)-1
print("Enter index between range 0 to ",end)
ind=int(input("ENter index "))

if ind<len(msg):

     if msg[ind] in msg:
         print("Character is ",msg[ind])
else:
     print("Please Enter  index in range ")


