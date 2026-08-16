num=input("Enter Number : ")
mid=len(num)//2
first=num[:mid]
second=num[mid:]
sum1=0
sum2=0

for i in first:
    sum1=sum1+int(i)
for j in second:
    sum2=sum2+int(j)
print("First Half : ",sum1)
print("Second Half : ",sum2)
if sum1==sum2:
    print("Perfect Number ")
else:
    print("Not A perfect Number ")
