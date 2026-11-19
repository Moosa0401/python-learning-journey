playerNumbers = {"Moosa" : 10, 
                 "Ahmed": 7, 
                 "Ibra": 4,
                 "Suhaib": 5}

print(playerNumbers)
print(playerNumbers["Ahmed"])

# print out keys by default
for player in playerNumbers:
    print(player)


for number in playerNumbers.values():
      print(number)


for player in playerNumbers:
        print(player, playerNumbers[player], sep=": ")
