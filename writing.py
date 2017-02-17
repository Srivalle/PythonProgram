file = open("newfile.txt", "w")

file.write("hello world in the new file")

file.write("and another line")

file.close()

file1 = open("newfile.txt" ,"r")
for line in file1:
    print(line)

file1.close()    
