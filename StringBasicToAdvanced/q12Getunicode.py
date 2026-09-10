msg=input("Enter your String : ")
ind=int(input("Enter index "))

if ind>len(msg):
    print("Please Enter index in range ")
else:



     if msg[ind] in msg:
        print(ord(msg[ind]))

