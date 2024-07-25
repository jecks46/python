import random

print("Who is win ballon dor?")
print("/nGuess players are win balloon dor")
players = input("/nEnter name of players by comma...")
players.split(",")
ran = random.randint(0,len(players)-1)
ran_player = players[ran]
print(f"/n{ran_player} is win ballon dor")

