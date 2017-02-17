import scrabble
class findingPalendrom:
   
    def findPalend(self):
        longest=""        
        for word in scrabble.wordlist:
            if list(word) == list(reversed(word)) and len(word)>len(longest):
                longest = word

        print(longest)


    def findPal(self):
        longest=""        
        for word in scrabble.wordlist:
            if word ==word[::-1] and len(word)>len(longest):
                longest = word

        print(longest)             
    

obj=findingPalendrom()
obj.findPalend()
obj.findPal()
