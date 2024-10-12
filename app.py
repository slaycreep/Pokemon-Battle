end_of_game =False #inititally we will consider that end of game is false
round=1 #starting 'turn' variable
player1_hp=50  #initial HP for P1
player2_hp=50  #initial HP for P2     

player1 = input("You Choose: ") #player 1 input
player2 = input("Gary Chooses: ") #player 2 input

while end_of_game == False: #while end of game is false, while loop will continue
#Checking possible conditions for end of game
  if player1_hp <= 0 and player2_hp <= 0:  #when its a tie
    end_of_game = True
    print("It's a tie!")
  elif player1_hp <= 0: #when player 2 wins
    end_of_game = True
    print(f"{player2} and Gary wins!")
  elif player2_hp <= 0: #when player 1 wins
    end_of_game = True
    print(f"{player1} and Ash wins!") 
  else: #when there is no possibility of the game ending it will continue the game                                     
    print(f"=== Turn {round} ===") #print statements for each round

  if end_of_game == True: #while loop will break if end of the game is true
    break

  if (player1=="Charmander" or player1 == "Cyndaquil") and (player2=="Totodile" or player2=="Squirtle"): #condition for fire X water
      player1_hp= player1_hp - 20*2 #water causes 2X damage on player1
      player2_hp = player2_hp - 20*0.5 #fire causes 0.5X damage on player2
      if player1_hp<0: #condition if health goes below 0
        player1_hp=0
      if player2_hp<0:#condition if health goes below 0
         player2_hp=0
      print(f"{player1} has {int(player1_hp)} hp left") #print statements for each round
      print(f"{player2} has {int(player2_hp)} hp left")
      round+=1 #round will increase by 1 for every turn by 1
  elif (player1=="Charmander" or player1 == "Cyndaquil") and (player2=="Bulbasaur" or player2=="Chikorita"): #condition for fire X grass
        player1_hp= player1_hp - 20*0.5
        player2_hp = player2_hp - 20*2
        if player1_hp<0:                                               #same as before
          player1_hp=0
        if player2_hp<0:
          player2_hp=0
        print(f"{player1} has {int(player1_hp)} hp left")  
        print(f"{player2} has {int(player2_hp)} hp left")
        round+=1    
  elif (player1=="Squirtle" or player1 == "Totodile") and (player2=="Charmander" or player2=="Cyndaquil"): #condition for water X fire
        player1_hp= player1_hp - 20*0.5
        player2_hp = player2_hp - 20*2
        if player1_hp<0:
          player1_hp=0                                              #same as before
        if player2_hp<0:
          player2_hp=0
        print(f"{player1} has {int(player1_hp)} hp left")  
        print(f"{player2} has {int(player2_hp)} hp left")
        round+=1  
  elif (player1=="Squirtle" or player1 == "Totodile") and (player2=="Chikorita" or player2=="Bulbasaur"): #condition for water X grass
          player1_hp= player1_hp - 20*2
          player2_hp = player2_hp - 20*0.5
          if player1_hp<0:
            player1_hp=0                                              #same as before
          if player2_hp<0:
            player2_hp=0
          print(f"{player1} has {int(player1_hp)} hp left")  
          print(f"{player2} has {int(player2_hp)} hp left")
          round+=1  
  elif (player1=="Bulbasaur" or player1 == "Chikorita") and (player2=="Charmander" or player2=="Cyndaquil"): #condition for grass X fire
          player1_hp= player1_hp - 20*2
          player2_hp = player2_hp - 20*0.5
          if player1_hp<0:
            player1_hp=0                                              #same as before
          if player2_hp<0:
            player2_hp=0
          print(f"{player1} has {int(player1_hp)} hp left")  
          print(f"{player2} has {int(player2_hp)} hp left")
          round+=1    
  elif (player1=="Bulbasaur" or player1 == "Chikorita") and (player2=="Squirtle" or player2=="Totodile"): #condition for grass X water
          player1_hp= player1_hp - 20*0.5
          player2_hp = player2_hp - 20*2
          if player1_hp<0:
            player1_hp=0                                               #same as before
          if player2_hp<0:
            player2_hp=0
          print(f"{player1} has {int(player1_hp)} hp left")  
          print(f"{player2} has {int(player2_hp)} hp left")
          round+=1 
  else: #condition for same type attack (fireXfire grassXgrass waterXwater)
          player1_hp= player1_hp - 20
          player2_hp = player2_hp - 20
          if player1_hp<0:
              player1_hp=0
          if player2_hp<0:
              player2_hp=0
          print(f"{player1} has {int(player1_hp)} hp left")  
          print(f"{player2} has {int(player2_hp)} hp left")
          round+=1 
