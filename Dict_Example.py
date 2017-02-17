State_capital={"TamilNadu":"Chennai","AndhraPradesh":"Vijayawada","Telugana":"Hydrabad","Maharastra":"Mumbai","Karnataka":"Bangalore","Kerala":"trivendrum"}
States =State_capital.keys()
#print(States)

import random
for i in [1,2,3,4,5]:
    state=random.choice(States)
    capital = State_capital[state]
    #print("capital" +capital)
    capital_guess= raw_input("What is the capital of "+state+"?   ")
    if capital_guess == "quit":
        break
    #print("capital_guess" +capital_guess)
    if capital_guess == capital:
        print("Nice Job")

    else:
        print("Incorrect , The correct Capital of "+ state+ "is" +capital+".")
        
print("All done")  
