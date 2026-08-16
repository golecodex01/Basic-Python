time = int(input("Total event duration in seconds: "))

hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60

print("Hours:", hours, ", Minutes:", minutes, ", Seconds:", seconds)