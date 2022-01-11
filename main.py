print('''
                                                                           
8b,dPPYba, 88       88 8b,dPPYba, 
88P'   "Y8 88       88 88P'   `"8a
88         88       88 88       88
88         "8a,   ,a88 88       88
88          `"YbbdP'Y8 88       88 
                                  

''')


print("Welcome to The Big Race!")
print("In addition to being first, your goal is to survive.\nOhh yeah, dont forget to collect items on the way!") 

start = input("Type 'start' to beging running! ").lower()

weapon = 0

if start == "start":
  direction = input("Two paths are approaching, you see the majority of people go to the left.\nWhere would you like to go? 'left' or 'right': ").lower()
  if direction == "left":
    print("Playing it safe. However the terrain has changed and you all are forced to cross through swamps.\nNot only has it slowed you down but you're all wet! No way you'll be able to catch up now.\nWatch out for the crocs. You lost!")
  elif direction == "right":
    chest = input("looks like the risk paid off. Dry land. You begin to see different colored chest as your running.\nWould you like to open the green, yellow or red one? ").lower()
    if chest == "yellow":
      print("This chest was empty")
    elif chest == "Green" or "Red":
      print("You found a weapon!")
      weapon += 1
    sleep = input("I'ts getting dark now and you need to rest.\nWould you like to sleep by a tree or in a cave? ").lower()
    if sleep == "tree" and weapon != 0:
      print("You're greeted by a pack of wolves at night, but with your weapon you managed to fend them off long enough for them to decide you werent worth it")
      water = input("It's now time to keep running! And it's beginning to get very hot.\nWant to stop and get water by the approaching lake? yes or no: ").lower()
      if water == "yes":
        print("You stop to drink water but all its done is slow you down. Maybe this water wasn't as fresh as you thought. You begin to feel sick. You lost!")
      elif water == "no":
        print("Good choice, wh knows how good that water was. And the finish line was closer than expected! You made it.\nCongratulations you win!")

    elif sleep == "tree" and weapon == 0:
      print("You were greeted by a pack of wolves at night.\nWith no weapon to defend your self it was quickly over. You lost!")
    if sleep == "cave":
      water = input("Not the most comfortable night but you survived.\nI'ts now time to keep running! The heat is kicking in.\nStop to get water by the approaching lake? yes or no: ").lower()
      if water == "yes":
        print("You stop to drink water but all its done is slow you down.\nMaybe this water wasn't as fresh as you thought.\nYou begin to feel sick. You lost!")
      if water == "no":
        print("Good choice, who knows how good that water was.\nAnd the finish line was closer than expected! You made it.\nCongratulations you win!")
  