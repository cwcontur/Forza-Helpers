file = open("hopefully_car_list.txt", "r")
# car_names = open("car_names.txt", "w")
# years = open("years.txt", "w")
# countries = open("countries.txt", "w")
# ratings = open("ratings.txt", "w")

data = []

for line in file:
    
    line = str(line)
    data.append(line)

pos = 0

# Car names = pos[0]
# Year = pos[1]
# Country = pos[2]
# Rating = pos[3]
count = 0
for items in data:

    if pos == 0:
        # car_names.write(items)
        count += 1

    # if pos == 2:
    #     # countries.write(items)
        
    # if pos == 3:
    #     # ratings.write(items)
    
    # if pos == 1:
    #     years.write(items)
    

    pos += 1
    if pos == 4:
        pos = 0   


print(count)
# years.close()
# ratings.close()
# countries.close()
# car_names.close()

        
