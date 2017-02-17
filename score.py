f = open("score.txt","w")

while True:

    participant = raw_input("Enter the Participant Name > ")
    if participant =="quit":
        break
    score = raw_input("Score of the "+ participant +" > ")
    f.write(participant +", "+ score +"\n")
    


f.close()    

