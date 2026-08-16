num=int(input("Enter Number "))
nextnum=num-1


while True:
    if num<=2:
       print("No Prime Exit ")
       break
    
    count=0
    for i in range(1,nextnum+1):
        if nextnum%i==0:
            count=count+1
    if count==2:
        print("previous prime ",nextnum)
        break
    nextnum=nextnum-1
