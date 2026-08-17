
# 3.
# Industrial Sensor Peak Energy Monitoring System

# Problem Statement

# A factory machine records energy consumption at regular intervals.

# A peak is defined as a value greater than or equal to its neighbors.

# Tasks:

# Find all peak energy values
# Compute sum of squares of peak values
# Compute average of peak values
# Return difference between max peak and min peak
# If no peaks, return -1

# Test Case 1

# Input:
# energy = [20, 40, 30, 60, 50]

# Output:
# Peaks = [40, 60]
# Sum of squares = 5200
# Average = 50
# Difference = 20

# Test Case 2

# Input:
# energy = [10, 20, 15, 25, 20, 30]

# Output:
# Peaks = [20, 25, 30]
# Sum of squares = 1525
# Average = 25
# Difference = 10

# Test Case 3

# Input:
# energy = [5]

# Output:
# Peaks = [5]
# Sum of squares = 25
# Average = 5
# Difference = 0
l=list(map(int, input("enter a list : ").split(",")))
n=len(l)

peak=-1
peakvalue=[]
sum=0
maxi=l[0]
mini=l[0]
sq=0

for i in range(n):

    if n==1:
        peakvalue.append(l[i])
        peak=i
        sum=l[i]
        sq=l[i]*l[i]
        maxi=l[i]
        mini=l[i]
        break

    elif i==0:
        if l[i]>=l[i+1]:
            peakvalue.append(l[i])
            sum=sum+l[i]
            sq=sq+(l[i]*l[i])
            peak=i
            maxi=l[i]
            mini=l[i]

    elif i==n-1:
        if l[i]>=l[i-1]:
            peakvalue.append(l[i])
            sum=sum+l[i]
            sq=sq+(l[i]*l[i])
            peak=i

            if l[i]>maxi:
                maxi=l[i]
            if l[i]<mini:
                mini=l[i]

    else:
        if l[i]>=l[i-1] and l[i]>=l[i+1]:
            peakvalue.append(l[i])
            sum=sum+l[i]
            sq=sq+(l[i]*l[i])
            peak=i

            if l[i]>maxi:
                maxi=l[i]

            if l[i]<mini:
                mini=l[i]

if peak!=-1:
    avg=sum/len(peakvalue)
    print("Peaks =", peakvalue)
    print("Sum of squares =", sq)
    print("Average =", avg)
    print("Difference =", maxi-mini)
else:
    print(-1)