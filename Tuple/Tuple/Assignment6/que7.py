n=int(input("Enter number of players: "))
players=[]

for i in range(n):
    player_id,player_name,runs=input().split()
    players.append((int(player_id),player_name,int(runs)))

print("All Players:")
for p in players:
    print(p)

highest=players[0]
lowest=players[0]
total=0

for p in players:
    total=total+p[2]

    if p[2]>highest[2]:
        highest=p

    if p[2]<lowest[2]:
        lowest=p

average=total/n

print("Highest Scorer:")
print(highest)

print("Lowest Scorer:")
print(lowest)

print("Total Runs:")
print(total)

print("Average Runs:")
print(average)

print("Players Scoring More Than 50 Runs:")
for p in players:
    if p[2]>50:
        print(p)