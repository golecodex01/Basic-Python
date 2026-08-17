
n = int(input("Enter N: "))
ages = list(map(int, input("Enter ages: ").split()))

k = int(input("Enter K: "))

count = 0

for i in range(n):
    for j in range(i + 1, n):
        if abs(ages[i] - ages[j]) == k:
            count = count + 1

print("Number of pairs:", count)