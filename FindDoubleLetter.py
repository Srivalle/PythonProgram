import scrabble
import string




class dobleletterword:
    
    vowels = "aeiou"
    def __init__(self):
        print("Hello")
    

# Print all words containing uu
    def findingDuble(self):
        for letter in string.ascii_lowercase:
       # wordlist = scrabble.wordlist()
            for word in scrabble.wordlist:
                if letter*2 in word:
                    print("word" ,word)


    def findingDoubleAlpha(self):
        for letter in string.ascii_lowercase:
            exists = False
           # print("letter",letter*2)
            for word in scrabble.wordlist:
                if letter*2 in word:
                    exists =True
                    break
            if not exists:
                print("There is no english word with double",letter)
    
##    def has_all_vowels(word):
##        for vowel in vowels:
##            if vowel not in word:
##                return False
##        return True           
        
    def findingVowels(self):
        for word in scrabble.wordlist:
             for vowel in vowels:
                 if vowel  in word:
                     print(word)


    def findingpalendrom(self):
        for word in scrabble.wordlist:
            is_palendrom=True
            for index in range(len(word)):
                if word[index] != word[-(index+1)]:
                    is_palendrom=False
            if is_palendrom:
                print(word)

                 
    def findingLongestPalendrom(self):
        longest ="" 
        for word in scrabble.wordlist:
            is_palendrom=True
            for index in range(len(word)):
                if word[index] != word[-(index+1)]:
                    is_palendrom=False
            if is_palendrom and len(word)>len(longest):
                longest = word
                    
        print(longest)


letter = dobleletterword()
#letter.findingDuble()
#letter.findingDoubleAlpha()
#letter.findingVowels()
#letter.findingpalendrom()
letter.findingLongestPalendrom()
                
