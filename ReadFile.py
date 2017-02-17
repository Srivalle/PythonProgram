f= open("cities.txt","r")

Cities = []
for line in f:
    line = line.strip()
    Cities.append(line)

f.close()
print(Cities)

print len(Cities)

for city in Cities:
    if city[0] =="A":
        print city
      

