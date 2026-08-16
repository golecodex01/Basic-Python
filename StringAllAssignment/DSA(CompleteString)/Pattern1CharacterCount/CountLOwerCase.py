text = input("Enter String: ")

count = 0

for ch in text:
    if 'a' <= ch <= 'z':
        count += 1

print("Lowercase:", count)