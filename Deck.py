import random

class Deck(object):
    def shuffle(self):
        suites =["Spades","Hearts","Diamond","Clubs"]
        ranks = ["1","2,","3",",4","5","6","7","8","9","10","Jack","Ace","King","Queen"]
        self.cards = []
        for suite in suites:
            for rank in ranks:
                self.cards.append(rank + " of " + suite)
        print("suites" +self.cards)  
        random.shuffle(self.cards)
        
    def deal(self):
        return self.cards.pop()

d = Deck()
d.shuffle()
print(d.deal())



        
                
                
