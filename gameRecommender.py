### Dataset ###
ratings = {
    'EntyXD': {
        'Minecraft': 5,
        'Terraria': 4.5,
        'Super Mario 64': 3,
        'GTA 5': 4,
        'Call of Duty': 4.5
    },
    'EnderKnight': {
        'Minecraft': 5,
        'Terraria': 3,
        'Super Mario 64': 5,
        'GTA 5': 4,
        'Call of Duty': 3
    },
    'Nallarku':{
         'Minecraft': 4.5,
        'Terraria': 4,
        'Super Mario 64': 5,
        'GTA 5': 5,
        'Call of Duty': 3.5
    },
    'Ayaan': {
         'Minecraft': 5,
        'Terraria': 5,
        'Super Mario 64': 5,
        'GTA 5': 1,
        'Call of Duty': 1
    },
    'Cychrone': {
         'Minecraft': 5,
        'Terraria': 3,
        'Super Mario 64': 4,
        'GTA 5': 3.5,
        'Call of Duty': 3
    },
    'ThunderBeast': {
         'Minecraft': 5,
        'Terraria': 2,
        'Super Mario 64': 2.5,
        'GTA 5': 4.5,
        'Call of Duty': 4
    },
    'Marco': {
         'Minecraft': 5,
        'Terraria': 3,
        'Super Mario 64': 3.5,
        'GTA 5': 4,
        'Call of Duty': 2.5
    },
    'Ronit': {
         'Minecraft': 5,
        'Terraria': 4,
        'Super Mario 64': 2,
        'GTA 5': 3,
        'Call of Duty': 3
    },
}
### Libraries
from math import sqrt

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

print(f"The  similarity score between EnderKnight and Cychrone is  {sim_distance(ratings, 'EnderKnight', 'Cychrone')}")


### Sorting the reviews ####
def topMatches(prefs, person, n=5, similarity=sim_distance):
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
 

name = input("For who do you want to see the similarity leaderboard for VG preferences? ")
if name in ratings:
    topMatches(ratings, name)
else: 
    print("Invalid Input")



### Recommendations code: 
## Get recommendations for a person by using weighted average
def getRecommendations(prefs, person, similarity = sim_distance):
    totals = {}
    simSums={}
    

   

        



