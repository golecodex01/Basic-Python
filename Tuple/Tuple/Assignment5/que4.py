# Find common elements in three sorted arrays

n1=int(input("Enter size of A: "))
A=list(map(int,input("Enter A: ").split()))

n2=int(input("Enter size of B: "))
B=list(map(int,input("Enter B: ").split()))

n3=int(input("Enter size of C: "))
C=list(map(int,input("Enter C: ").split()))

i=0
j=0
k=0

while i<n1 and j<n2 and k<n3:
    if A[i]==B[j] and B[j]==C[k]:
        print(A[i],end=" ")
        value=A[i]
        while i<n1 and A[i]==value:
            i=i+1
        while j<n2 and B[j]==value:
            j=j+1
        while k<n3 and C[k]==value:
            k=k+1

    elif A[i]<B[j]:
        i=i+1

    elif B[j]<C[k]:
        j=j+1

    else:
        k=k+1