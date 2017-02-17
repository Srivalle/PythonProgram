import time

##f=open("sonnet_words.txt","r").readlines()
##
##sonnets=[]
##for line in f:
##    line =line.strip()
##    sonnets.append(line)
##
###f.close()    
##
##print("sonnets",sonnets)    

my_words = [elt.strip() for elt in open("sonnet_words1.txt", "r").readlines()]
#len = my_words.len()

#print("My words ",my_words)
word_list = [elt.strip() for elt in open("sowpod1.txt", "r").readlines()]
word_dict = dict((elt,1) for elt in word_list)

print( "Word Dict" , word_dict)
print( "Word list" , word_list)
counter = 0

start = time.time()
for word in my_words:
    if word not in word_dict:
        print(word)
        counter += 1

stop = time.time()

print("Total new words: %d" % counter)
print("Total Elapsed time : %1f seconds" %(stop-start))
