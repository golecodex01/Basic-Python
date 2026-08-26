'''1. Count Pairs with Difference K

A company records the ages of employees. Find how many pairs of employees have an age difference exactly equal to K.

Problem Statement:

Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.

Example:

Input:

N = 5
K = 2
ages[] = {1, 5, 3, 4, 2}

Output:

3

Explanation:

(1,3), (3,5), (2,4)


'''

age=list(map(int,input("Enter the ages of employees separated by space : ").split()))
count=0
k=int(input("Enter the value of K : "))
for i in range(len(age)):
    for j in range(i+1,len(age)):
        if abs(age[i]-age[j])==k:
            count+=1
print("The number of pairs with age difference exactly equal to K is :",count)


