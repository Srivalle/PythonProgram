import sqlite3

connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()
cursor.execute("select game from category order by Random() limit 1")
results= cursor.fetchall()
game_id =results[0][0]

print("Categorues for game Id #%d:" % (game_id,))

query = """select name,round from category where game=%d order by round""" %(game_id,)
cursor.execute(query)
results =cursor.fetchall()

print("Results ", results)

for result in results:
    name,round  =result
    #round =result[1]
    print("Round #%d: %s" %(round,name))


connection.close()    
    
