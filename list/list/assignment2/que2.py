
# 2.
# Smart City Traffic Peak Load Analyzer

# Problem Statement

# A smart city monitors traffic density at different time intervals in a day.

# An element is called a peak traffic point if it is greater than or equal to its adjacent elements.

# You are given an array traffic[] of size N.

# Tasks:

# Find all peak elements
# Calculate the sum of all peak traffic values
# Find the product of all peak traffic values
# Return the maximum peak value

# Note:
# If only one element exists, it is the only peak.

# Test Case 1

# Input:
# traffic = [10, 50, 30, 70, 60, 90, 80]

# Output:
# Peaks = [50, 70, 90]
# Sum = 210
# Product = 315000
# Max Peak = 90

# Test Case 2

# Input:
# traffic = [100, 200, 150, 180, 170]

# Output:
# Peaks = [200, 180]
# Sum = 380
# Product = 36000
# Max Peak = 200

# Test Case 3

# Input:
# traffic = [5]

# Output:
# Peaks = [5]
# Sum = 5
# Product = 5
# Max Peak = 5



l=list(map(int, input("enter a list").split(",")))
n=len(l)
peak=-1
peakvalue=[]
sum=0
product=1
maxi=l[0]

for i in range(n):
    if n==0:
        if n==1 or l[i]>=l[i-1]:
            peakvalue.append(l[i])
            peak=i
            sum=i
            product=i
            maxi=[i]
            break
    elif i==n-1:
        if l[i]>=l[i-1]:
            peakvalue.append(l[i])
            product=l[i]
            sum=l[i]
            peak=i
            maxi=l[i]
            break
    else:
        if l[i]>=l[i-1] and l[i]>=l[i+1]:
            peakvalue.append(l[i])
            sum=sum+l[i]
            product=product*l[i]
            peak=i
            if l[i]>maxi:
                maxi=l[i]
if peak!=-1:
    print(peakvalue)   
    print(sum)   
    print(product)   
    print(maxi)