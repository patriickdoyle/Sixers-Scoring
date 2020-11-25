#sixers_dictionary
#Assignment for CSCI 111-900
#Last edited 10/7/19 by Pat Doyle

points_dict  = dict(Harris = 24, Butler = 11, Embiid = 31, Simmons = 15, Reddick = 9, Scott = 8, Ennis = 7, Marjanovic = 4, Bolden = 1, McConnell = 2)

#Dictionary with player names and the points they scored

for player, points in points_dict.items(): #for loop defines key as players and value as points in the dictionary
    
    total = sum(points_dict.values())
    
    high_score = max(points_dict.values())

    #defines variables to find the total points scored and the highest individual scoring value
    
    if points == high_score:
        leading_scorer = player #if statement assigns variable to the player who scored the most points

    print(player, ':', points, 'points') #prints list of players and their points scored
    
print("The Sixers scored ", total, "points.")
print(leading_scorer , "was the team's leading scorer.")

#prints total points and the name of the leading scorer

print("\n Clap your hands \n Everybody \n For Philadelphia \n 76ers")
print("\n Stomp your feet \n Everybody \n For Philadelphia \n 76ers")
print("\n Here they come \n Philadelphia \n On the run \n Stand up and cheer!")
print("\n Number 1 \n Philadelphia \n Here they come \n Team of the year!")
print("\n 1 \n 2 \n 3 \n 4 \n 5 \n Sixers!")
print("\n 10 \n 9 \n 8 \n 76ers!")

#TrustTheProcess




    
    
