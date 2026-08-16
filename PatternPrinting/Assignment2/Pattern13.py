n=int(input("Enter a Number :"))
i=1
while i<=n:
      ch=64
      j=1
      while j<=i:
            print(chr(ch+j).lower() ,end=" ")

            j=j+1
      i=i+1
      print()
