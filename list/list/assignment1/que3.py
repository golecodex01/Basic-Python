
# 3.
# # Assignment: Prime Number Analyzer using List (Python)

# ## Scenario

# A coaching institute stores student lucky numbers in a Python List.
# Your task is to analyze the list and identify prime numbers for a scholarship selection process.

# You must iterate through every element of the list and perform prime number analysis.

# ---

# # Requirements

# Write a Python program to:

# 1. Store integer values in a List
# 2. Iterate through all elements of the List
# 3. Check whether each number is prime or not
# 4. Display all prime numbers
# 5. Count total prime numbers
# 6. Count total non-prime numbers
# 7. Find the largest prime number from the List
# 8. Store all prime numbers into another List
# 9. Sort the prime numbers in ascending order and display them

l=list(map(int,input("Enter a list: ").split()))
prime=[]
primecount=0
nonprimecount=0
greater=0

for i in l:
    count=0
    if i>greater:
        greater=i
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i)
        prime.append(i)
        prime_count+=1
    else:
        nonprimecount+=1


print("Prime Numbers :",prime)
print("Total Prime Numbers :",primecount)
print("Total Non-Prime Numbers :",nonprimecount)
if prime:
    print("Largest Prime Number :",greater)
else:
    print("No Prime Number")

prime.sort()
print("Sorted Prime Numbers :",prime)