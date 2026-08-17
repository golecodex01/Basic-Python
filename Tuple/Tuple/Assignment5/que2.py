
# 2.
# Secure Password Analysis

# A cybersecurity team wants to identify pairs of passwords having no common characters.

# Problem Statement:

# Given N strings, count the number of pairs that do not share any common character.

# Example:

# Input

# N = 4
# passwords[] = {"abc", "de", "fg", "ad"}

# Output

# 3

# Explanation

# ("abc","de")
# ("abc","fg")
# ("de","fg")

# Secure Password Analysis

n = int(input("Enter N: "))

passwords = []

for i in range(n):
    x = input("Enter password: ")
    passwords.append(x)

count = 0

for i in range(n):
    for j in range(i + 1, n):

        common = False

        for ch in passwords[i]:
            if ch in passwords[j]:
                common = True
                break

        if common == False:
            count = count + 1

print("Number of pairs:", count)