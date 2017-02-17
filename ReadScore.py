file = open("score.txt", "r")

participants ={}

for line in file:
    entry = line.strip().split(",")
    participant = entry[0]
    score = entry[1]
    participants[participant]=score



file.close()
print(participants)
