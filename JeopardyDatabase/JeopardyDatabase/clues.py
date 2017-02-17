import sqlite3

connection =sqlite3.connect("jeopardy.db")
cursor = connection.cursor()
cursor.execute("Select text ,answer , value from clue limit 5")
results = cursor.fetchall()

for clue in results:
    text,answer,value = clue
    #answer =clue[1]
    #$value =clue[2]

    print("[$%s]" %(value,))
    print("Question:%s" %(text,))
    print ("Answer : %s" %(answer,))
    print("")
