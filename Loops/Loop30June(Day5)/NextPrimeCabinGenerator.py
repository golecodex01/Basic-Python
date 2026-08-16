'''Next Prime Cabin Number Generator
A luxury hotel gives only prime numbered cabins to VIP guests.
Manager enters the last allotted cabin numbe
System must find the next available prime cabin number.
Write a program using loops.
Input:
24
Output:
Next Prime Cabin = 29 '''


n=int(input("ENter a Number "))

a=n+1

while True:
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c=c+1
    if c==2:
        print("Next Prime Cabin =",a)
        break
    a=a+1