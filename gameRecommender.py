### Dataset ###
ratings = {
    'EntyXD': {
        'Minecraft': 5,
        'Terraria': 4.5,
        'Super Mario 64': 3,
        'Grand Theft Auto V': 4,
        'Call of Duty': 4.5,
        'Geometry Dash': 4,
        'Among Us': 2.5,
        'Brawl Stars':3.5,
        'Fortnite':1,
        'Roblox':2,
        'Valorant':1.5

    },
    'EnderKnight': {
        'Minecraft': 5,
        'Terraria': 3,
        'Super Mario 64': 5,
        'Grand Theft Auto V': 4,
        'Call of Duty': 3
    },
    'Nallarku':{
         'Minecraft': 4.5,
        'Terraria': 4,
        'Super Mario 64': 5,
        'Grand Theft Auto V': 5,
        'Call of Duty': 3.5
    },
    'Ayaan': {
         'Minecraft': 5,
        'Terraria': 5,
        'Super Mario 64': 5,
        'Grand Theft Auto V': 1,
        'Call of Duty': 1
    },
    'Cychrone': {
         'Minecraft': 5,
        'Terraria': 3,
        'Super Mario 64': 4,
        'Grand Theft Auto V': 3.5,
        'Call of Duty': 3,
        'Geometry Dash': 4,
        'Among Us': 3,
        'Brawl Stars': 4,
        'Fortnite': 4,
        'Roblox': 4,
        'Valorant': 3,
        'Any EA Game': 3.5,
    },
    'ThunderBeast': {
         'Minecraft': 5,
        'Terraria': 2,
        'Super Mario 64': 2.5,
        'Grand Theft Auto V': 4.5,
        'Call of Duty': 4,
        'Geometry Dash': 1,
        'Among Us': 2,
        'Brawl Stars': 3.5,
        'Fortnite': 5,
        'Roblox': 2,
        'Valorant': 2,
        'Any EA Game': 3
    },
    'Marco': {
         'Minecraft': 5,
        'Terraria': 3,
        'Super Mario 64': 3.5,
        'Grand Theft Auto V': 4,
        'Call of Duty': 2.5
    },
    'Ronit': {
         'Minecraft': 5,
        'Terraria': 4,
        'Super Mario 64': 2,
        'Grand Theft Auto V': 3,
        'Call of Duty': 3
    },
    'ZG3': {
        'Minecraft': 4,
        'Terraria': 2,
        'Super Mario 64': 3.5,
        'Grand Theft Auto V': 1,
        'Call of Duty': 3
    },
    'Boandme': {
         'Minecraft': 0,
        'Terraria': 0,
        'Super Mario 64': 0,
        'Grand Theft Auto V': 0,
        'Call of Duty':0
    },
    'Ruhaan': {
        'Minecraft': 4,
        'Terraria': 3.5,
        'Super Mario 64': 3,
        'Grand Theft Auto V': 4,
        'Call of Duty': 4
    },
    'Ishaan': {
        'Minecraft': 4.5,
        'Terraria': 4.5,
        'Among Us': 3.5,
        'Fortnite':3.5

    },
    'Shayguy': {
        'Minecraft' :4.5,
        'Terraria': 3,
        'Super Mario 64': 4,
        'Grand Theft Auto V': 4,
        'Call of Duty':3.5,
        'Geometry Dash': 3,
        'Among Us': 1.5 ,
        'Brawl Stars': 2.5,
        'Fortnite': 4,
        'Roblox':3.5,
        'Valorant':4.5,
        'Any EA Game':4

    },
    'Buger': {
        'Minecraft': 4.5,
        'Terraria': 3,
        'Super Mario 64': 3.5,
        'Grand Theft Auto V': 3,
        'Call of Duty': 2,
        'Geometry Dash': 4,
        'Among Us': 3,
        'Brawl Stars': 2,
        'Fortnite': 2.5,
        'Roblox': 2.5,
        'Valorant': 2
    },
    'NMkebab': {
        'Minecraft': 4.5,
        'Terraria': 2.5,
        'Super Mario 64': 3,
        'Grand Theft Auto V': 2,
        'Call of Duty': 3.5,
        'Geometry Dash': 4,
        'Among Us': 3.5,
        'Brawl Stars': 3,
        'Fortnite': 2.5,
        'Roblox': 2.5,
        'Valorant': 3.5,
        'Any EA Game': 4.5
    },
    'Messithegoat': {
        'Minecraft' : 5,
        'Terraria': 5,
        'Super Mario 64': 4,
        'Geometry Dash': 1,
        'Fortnite': 1,
        'FC 25': 2
    },
    'Cheerios': {
        'Minecraft': 5,
        'Terraria': 1,
        'Super Mario 64': 3.5,
        'Grand Theft Auto V': 3,
        'Call of Duty': 3.5,
        'Geometry Dash': 4,
        'Among Us': 3,
        'Brawl Stars': 4,
        'Fortnite': 4,
        'Roblox': 3,
        'Valorant': 3.5,
        'Any EA Game': 3.5
    }


}
### Libraries
from math import sqrt
import pandas as pd
import seaborn
import matplotlib
import matplotlib.pyplot as plt

### Code here ####
def sim_distance(prefs, person1, person2):
    shared_items = {}
    ## Get list of shared items ###
    for item in prefs[person1]:
        if item in prefs[person2]:
            shared_items[item]=1

    ## if no ratings in common, return 0
    if len(shared_items) == 0:
        return 0
    
    ### Find the similarity score between two ppl ## 
    sum_of_squares = 0
    for item in shared_items:
        diff = prefs[person1][item] - prefs[person2][item]
        sum_of_squares += diff * diff

    return 1/(1+sqrt(sum_of_squares))

##print(f"The  similarity score between EnderKnight and Cychrone is  {sim_distance(ratings, 'EnderKnight', 'Cychrone')}")


### Sorting the reviews ####
def topMatches(prefs, person, n=6, similarity=sim_distance):
    scores = []  
    for other in prefs:
        if other != person:
            
            scores.append((similarity(prefs, person, other), other))
    scores.sort()     
    scores.reverse()
    print()
    print(f"--------- VG Prefs Similarity Rankings to {person}")
    for i in range(0, len(scores)):
        print(f"{i}: {scores[i]}")   
    return scores
 

##name = input("For who do you want to see the similarity leaderboard for VG preferences? ")
##if name in ratings:
##    topMatches(ratings, name)
##else: 
##    print("Invalid Input")



### Recommendations code: 
## Get recommendations for a person by using weighted average
def getRecommendations(prefs, person, similarity=sim_distance):
    totals = {}
    simSums = {}
    rankings = []
    for other in prefs:
        if other == person:
            continue

        sim = similarity(prefs, person, other)
        if sim <= 0:
            # Skip users who are not similar
            continue

        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item] == 0:
                totals.setdefault(item, 0)
                totals[item]+=prefs[other][item]*sim

                ## Sum
                simSums.setdefault(item, 0)
                simSums[item] += sim
              
    # Build normalized  list
    
    rankings = [(total/simSums[item], item)for item, total in totals.items()]

    rankings.sort(reverse=True)
    print()
    print("\n-------- VG leaderboard(17 reviews) ---------------")
    for i in range(0, len(rankings)):
        print(f"{i+1}: {rankings[i][1]} - {round(rankings[i][0], 2)}")   
    

    return rankings
        

getRecommendations(ratings,'Boandme', similarity = sim_distance)
        

###### Similarity Matrix Creation ####
people = []
for i in ratings:
    people.append(i)

# Create an empty dictionary to hold the similarity rows
similarity_matrix = {}

# Loop through each person to create rows
for person1 in people:
    row = [] 
    for person2 in people:
        score = sim_distance(ratings, person1, person2)
        row.append(round(score,2))
    similarity_matrix[person1] = row

df = pd.DataFrame(similarity_matrix, index=people)
plt.figure(figsize=(12, 8))  # Adjust figure size
seaborn.heatmap(df, annot=True, cmap="coolwarm", square=True, cbar=True)
plt.title("Similarity Heatmap")
plt.show()


   

        



