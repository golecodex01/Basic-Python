#**7. Count Even Digits**
#A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
#rite a program to **count the number of even digits in a given number using loops**.

#@Input: 123456
#Output: Even digits count = 3

num=int(input("ENter a Number :"))
count=0
while num>0:
    digit=num%10
    if digit%2==0:
        count=count+1
    num=num//10

print("Count of Even Digits in Number is :",count)

