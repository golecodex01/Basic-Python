# 8.
# MATRIX PATTERN DETECTION SYSTEM

# A satellite monitoring center stores signal strengths in matrix form. Engineers want to identify special patterns in the matrix.

# Menu
# 1. Count Even Numbers Above Main Diagonal
# 2. Count Odd Numbers Below Main Diagonal
# 3. Display Boundary Elements
# 4. Exit
# Requirements
# Choice 1 – Count Even Numbers Above Main Diagonal

# Count all even numbers where:

# column > row
# Choice 2 – Count Odd Numbers Below Main Diagonal

# Count all odd numbers where:

# row > column
# Choice 3 – Display Boundary Elements

# Display all elements present on:

# First Row
# Last Row
# First Column
# Last Column

# without repeating corner elements.

# Sample Input
# 1 2 3
# 4 5 6
# 7 8 9
# Output
# Even Numbers Above Main Diagonal = 2
# (2, 6)

# Odd Numbers Below Main Diagonal = 1
# (7)

# Boundary Elements:
# 1 2 3 6 9 8 7 4
r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))

matrix=[]

for i in range(r):
    row=list(map(int,input().split()))
    matrix.append(row)

while True:
    print("1. Count Even Numbers Above Main Diagonal")
    print("2. Count Odd Numbers Below Main Diagonal")
    print("3. Display Boundary Elements")
    print("4. Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        count=0
        values=[]

        for i in range(r):
            for j in range(c):
                if j>i and matrix[i][j]%2==0:
                    count=count+1
                    values.append(matrix[i][j])

        print("Even Numbers Above Main Diagonal =",count)
        print(values)

    elif choice==2:
        count=0
        values=[]

        for i in range(r):
            for j in range(c):
                if i>j and matrix[i][j]%2!=0:
                    count=count+1
                    values.append(matrix[i][j])

        print("Odd Numbers Below Main Diagonal =",count)
        print(values)

    elif choice==3:
        print("Boundary Elements:")

        for j in range(c):
            print(matrix[0][j],end=" ")

        for i in range(1,r):
            print(matrix[i][c-1],end=" ")

        for j in range(c-2,-1,-1):
            print(matrix[r-1][j],end=" ")

        for i in range(r-2,0,-1):
            print(matrix[i][0],end=" ")

        print()

    elif choice==4:
        break

    else:
        print("Invalid Choice")