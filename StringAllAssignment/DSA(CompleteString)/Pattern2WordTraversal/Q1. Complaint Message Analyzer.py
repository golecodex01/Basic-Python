msg=input("Enter your message : ")

new=""

for i in range(len(msg)):
    if i==0 and msg[i]>='a' and msg[i]<='z':
        new=new+char(ord(msg[i])-32)
    elif msg[i-1]==" ":
        
    