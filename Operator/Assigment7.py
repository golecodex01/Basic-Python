runs = 275
overs = 48.3

fullovers = int(overs)
balls = int((overs - fullovers) * 10)

totalballs = fullovers*6+balls
runrate = runs /(totalballs/6)

print("Total Balls =",totalballs)
print("Run Rate =",round(runrate,2))