
# 2.Employee Salary Processing
# Store employee salaries in a List and calculate details.

# Requirements:

# Store salaries
# Find average salary
# Display salaries greater than average
# Remove salaries below 15000

# Test Cases:

# Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
# Input: [15000, 15000, 15000] → Average = 15000
# Input: [5000, 7000] → Remaining List = []
l=list(map(int,input("enter salary").split()))
sum=0
count=0

for i in l:
    sum=sum+i
    count=count+1
avg=int(sum/count)
print(avg)
new=[]
for i in l:
    if i>avg:
        greater=i
    if i<15000:
        new.append(i)
        
print("Average = ",avg,"Above Average = ",greater,"Remaining list = ",new)
