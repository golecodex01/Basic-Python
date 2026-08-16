word=input("Enter a String ")
start=0
rev=""
end=len(word)-1
while end>=start:
    rev=rev+(word[end])
    end=end-1
print("Reversible ",rev)
