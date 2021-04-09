"""
-------------------------------------------------------------------------------
Name:   Jumanji.py
Purpose:  A short multiple choice game where the user's input's effect the game's outcome and text.
 
Author: Ku.T
 
Created:  25, 3, 2021
------------------------------------------------------------------------------
"""
import random

#Introduction
print("")
print("----------------------------------")
print("| Welcome to Jumanji, traveller! |")
print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
print("")

print("To begin, please select your character using the alphabet corresponding to the choice!")
print("")

print("A) Microsoft Defender")
print("B) Norton 360")
print("C) BitDefender Antivirus") 
print("D) McAfee Total Protection")

char = 0
name = ""
print("")

#Character Selection

choice = input("I select: ")

while choice != "A" and choice != "B" and choice != "C" and choice != "D":
    print("Please chose a character avaliable (Choices are case sensitive)")
    choice = input("I select: ")

if choice == "A":
  name = "Microsoft Defender"
  char = 1

elif choice == "B":
  name = "Norton 360"
  char = 2

elif choice == "C":
  name = "BitDefender Antivirus"
  char = 3

else: 
  choice == "D"
  name = "McAfee Total Protection"
  char = 4
  
#Greetings and stat introduction
print("")
print("Ah yes, hello", name, "!")
print("")
print("Your stats are from a range of 0 - 10")
print("")

strength = 0
speed = 0
reliability = 0

#Character profile setup
print("Your stats are:")
print("")

if char == 1:
  strength = 8
  speed = 4
  reliability = 6

elif char == 2:
  strength = 9
  speed = 3
  reliability = 6

elif char == 3:
  strength = 5
  speed = 5
  reliability = 8

else:
  strength = 9
  speed = 3
  reliability = 6

#Introduction and tutorial
print("Strength:", strength, "    (Attack damage)")
print("Speed:", speed, "       (Chance to dodge enemy attack) ")
print("Reliability:", reliability, " (Chance to hit your attack) ")

print("_______________")
print("")
print("*Tutorial*")
print("")
print("You will have the option of a closed ranged attack which deals more damage but is less reliable")
print("Or a ranged attack which deals less damage but is more reliable.")
print("This will scale with your characters base stats")
print("")
print("Your health will recharge after every battle.")
print("On top of this, you will have two firewall consumables, which will restore a portion of your health mid-battle.")
print("_______________")
print("")
input("Press enter to continue: ")
print("")
print("Your quest is to put an end to the malicious viruses that have been attacking the computer's software.")
print("")
print("Good luck!")
print("")
print("You come across a path splitting two ways. To the left is a war-torn field. To the right is the forest")
print("")

#Deciding fights
fight_1 = True
path_1 = ""

choice_1 = input("Where do you choose to go?: ")

while choice_1 != "left" and choice_1 != "right":
    print("Please chose left or right")
    choice_1 = input("Where do you choose?: ")
    
if choice_1 == "right":
  fight_1 = True
  path_1 = "right"

else:
  choice_1 == "left"
  fight_1 = False
  path_1 = "left"

print("")
print("You walk down the", path_1, "pathway.")
print("")

#Character attack damage setup
character_health = 50
adware_health = 10

c_r_s = strength - 1
c_r_r = reliability - 2

r_a_s = strength - 3
r_a_r = reliability

firewall = 2

#Fight 1 user decisons
if fight_1 == True:
  print("You come upon your first enemy.")
  print("")
  print("Adware has appeared!")
  print("Adware Health:", adware_health)
  print(name, "Health:", character_health)
  while adware_health > 0:
    print("")
    print("What will you do?")
    print("")
    print("A) Close ranged  (s:", strength - 1, ") (r:", reliability - 2,")")
    print("B) Ranged attack (s:", strength - 3, ") (r:", reliability, ")")
    print("C) Use Firewall count:", firewall)
    print("")
    move = input("Move: ")
    print("")

    #User correct statemnt
    while move != "A" and move != "B" and move != "C":
      print("Please choose a given prompt above.")
      move = input("Move: ")
      print("")

    #Closed range attack chances
    if move == "A":
      roll = random.randint(0,10)
      if roll <= c_r_r:
        print("You hit Adware with a close ranged attack!")
        adware_health = adware_health - c_r_s
        print("Adware Health:", adware_health, "/ 10")
        print("")
        if adware_health > 0: 
          print("Adware attacks!")
          print("")
          enemy_roll = random.randint(0,10)
          if enemy_roll <= 5 - speed:
            print("Adware hit you!")
            character_health = character_health - 5
            print("Your health:", character_health, "/ 50")
          else:
            if adware_health > 0:
              print("Adware missed!")
        else:
          print("Adware has been defeated!")
          print("Congradulations you obtained an extra Firewall charge!")

      #If the character misses
      else:
          print("You missed your close ranged attack!")
          print("")
          print("Adware attacks!")
          print("")
          enemy_roll = random.randint(0,10)
          if enemy_roll <= 5 - speed:
            print("Adware hit you!")
            character_health = character_health - 5
            print("Your health:", character_health, "/ 50")
          else:
            if adware_health > 0:
              print("Adware missed!")

    #Ranged attack chances
    elif move == "B":
      roll = random.randint(0,10)
      if roll <= r_a_r:
        print("You hit Adware with a ranged attack!")
        adware_health = adware_health - r_a_s
        print("Adware Health:", adware_health, "/ 10")
        print("")
        if adware_health > 0: 
          print("Adware attacks!")
          print("")
          enemy_roll = random.randint(0,10)
          if enemy_roll <= 5 - speed:
            print("Adware hit you!")
            character_health = character_health - 3
            print("Your health:", character_health, "/ 50")
          else:
            if adware_health > 0:
              print("Adware missed!")
        else:
          print("Adware has been defeated!")
          print("Congradulations you obtained an extra Firewall charge!")

      #If the character misses
      else:
          print("You missed your ranged attack!")
          print("")
          print("Adware attacks!")
          print("")
          enemy_roll = random.randint(0,10)
          if enemy_roll <= 5 - speed:
            print("Adware hit you!")
            character_health = character_health - 3
            print("Your health:", character_health, "/ 50")
          else:
            if adware_health > 0:
              print("Adware missed!")

    #Health regeneration calculations
    else:
      if move == "C":
        if firewall >= 1:
          firewall = firewall - 1
          if character_health >= 25:
            character_health = 50
            print("FIREWALL CONSUMED")
            print(name, "Health:", character_health)

          else:
            character_health = character_health + 25
            print("FIREWALL CONSUMED")
            print(name, "Health:", character_health)
        
        else:
          print("You have no more Firewalls!")

#Left path outcome
else:
  print("You come across a small shrine with a relic inside.")
  print("Congradulations your strength has increased by +2!")
  strength = strength + 2

print("")
input("Press enter to continue: ")

#Questionare
print("")
print("You come across a giant door on the side of a mountain with enscribed words.")
print('It says, "To open the door you must answer the following question"')
print("")
print('"Which of the following is a famous example of Ransomware?"')
print("")
print("A) SadFace")
print("B) tREX")
print("C) GoldenWind")
print("D) WannaCry")
print("")
choice = input("Your answer: ")
print("")

fight_2 = True

#User correctment
while choice != "A" and choice != "B" and choice != "C" and choice != "D":
  print("Please choose a valid answer")
  choice = input("Your answer: ")

#If the user gets the answer correct
if choice == "D":
  print("Correct answer")
  fight_2 = False

#If the user gets the answer wrong
else:
  print("Incorrect answer")
  print("*You hear rumbling from above*")
  print("")
  input("Press enter to continue: ")
  print("")
  print("A browser highjacker appears!")
  print("")

#Enemy and player set up
character_health = 50
browser_health = 25

if fight_1 == True:
  firewall = 3
else:
  firewall = 2

character_alive = True

#Updates stats with any new relics or upgrades
c_r_s = strength - 1
c_r_r = reliability - 2

r_a_s = strength - 3
r_a_r = reliability

#Fight 2
if fight_2 == True:
  print("Browser highjacker Health:", browser_health)
  print(name, "Health:", character_health)
  while browser_health > 0 and character_alive == True:
    print("")
    print("What will you do?")
    print("")
    print("A) Close ranged  (s:", strength - 1, ") (r:", reliability - 2,")")
    print("B) Ranged attack (s:", strength - 3, ") (r:", reliability, ")")
    print("C) Use Firewall count:", firewall)
    print("")
    move = input("Move: ")
    print("")

    #User correct statemnt
    while move != "A" and move != "B" and move != "C":
      print("Please choose a given prompt above.")
      move = input("Move: ")
      print("")

    #Closed range attack chances
    if move == "A":
      roll = random.randint(0,10)
      if roll <= c_r_r:
        print("You hit Browser highjacker with a close ranged attack!")
        browser_health = browser_health - c_r_s
        print("Browser highjacker Health:", browser_health, "/ 25")
        print("")
        if browser_health >= 0: 
          print("Browser highjacker attacks!")
          print("")
          enemy_roll = random.randint(0,10)
          if enemy_roll <= 8 - speed:
            print("Browser highjacker hit you!")
            character_health = character_health - 8
            print("Your health:", character_health, "/ 50")
            if character_health <= 0:
              print("")
              print("You have died")
              character_alive = False

          else:
            if browser_health >= 0:
              print("Browser highjacker missed!")
        else:
          print("The Browser highjacker has been defeated!")
          input("Press enter to continue: ")

      #If the player misses
      else:
          print("You missed your close ranged attack!")
          print("")
          print("Browser highjacker attacks!")
          print("")
          enemy_roll = random.randint(0,10)
          if enemy_roll <= 8 - speed:
            print("Browser highjacker hit you!")
            character_health = character_health - 8
            print("Your health:", character_health, "/ 50")
            if character_health <= 0:
              print("")
              print("You have died")
              character_alive = False
          else:
            print("Browser highjacker missed!")

    #Ranged attack chances
    elif move == "B":
      roll = random.randint(0,10)
      if roll <= r_a_r:
        print("You hit Browser highjacker with a ranged attack!")
        browser_health = browser_health - r_a_s
        print("Browser highjacker Health:", browser_health, "/ 25")
        print("")
        if browser_health > 0: 
          print("Browser highjacker attacks!")
          print("")
          enemy_roll = random.randint(0,10)
          if enemy_roll <= 7 - speed:
            print("Browser highjacker hit you!")
            character_health = character_health - 6
            print("Your health:", character_health, "/ 50")
            if character_health <= 0:
              print("")
              print("You have died")
              character_alive = False

          #If the enemy misses
          else:
            if browser_health >= 0:
              print("Browser highjacker missed!")

        #When the browser highjacker dies this plays
        else:
          print("The Browser highjacker has been defeated!")
          input("Press enter to continue: ")

      #If you miss your ranged attack
      else:
          print("You missed your ranged attack!")
          print("")
          print("Browser highjacker attacks!")
          print("")
          enemy_roll = random.randint(0,10)
          if enemy_roll <= 7 - speed:
            print("Browser highjacker hit you!")
            character_health = character_health - 6
            print("Your health:", character_health, "/ 50")
            if character_health <= 0:
              print("")
              print("You have died")
              character_alive = False

          #If the enemy misses
          else:
            if browser_health >= 0:
              print("Browser highjacker missed!")

    #Health regeneration calculations
    else:
      if move == "C":
        if firewall >= 1:
          firewall = firewall - 1
          if character_health >= 25:
            character_health = 50
            print("FIREWALL CONSUMED")
            print(name, "Health:", character_health)

          else:
            character_health = character_health + 25
            print("FIREWALL CONSUMED")
            print(name, "Health:", character_health)
          
        else:
           print("You have no more Firewalls!")

#Adventure text
print("*The door rumbles and opens to a long and dark mountainside cave*")
print("")
print("You walk down it")
print("")
print("You have the option to travel towards the temple or treasury inside.")
choice = input("Where do you choose to go?: ")
print("")

#User correction
while choice != "temple" and choice != "treasury":
  print("Please type either temple or treasury.")
  choice = input("Where do you choose to go?: ")

#Temple path
if choice == "temple":
  print("You go towards the temple shrine.")
  print("")
  print("Once inside, you see an enemy guarding the offerings.")
  print("")
  print("Do you attack him or do try and sneak into the prayer room?")
  print("")
  choice = input("Please type attack or sneak: ")
  print("")

  #User correction
  while choice != "sneak" and choice != "attack":
    print("Please type either sneak or attack.")
    choice = input("What do you do?: ")

  #Sets up a fight if the user chooses to attack
  if choice == "attack":

    character_health = 50
    spyware_health = 35

    #Updates stats with any new relics or upgrades
    c_r_s = strength - 1
    c_r_r = reliability - 2

    r_a_s = strength - 3
    r_a_r = reliability

    #Firewall counting
    if fight_1 == True:
      firewall = 3
    else:
      firewall = 2
  
    #Fight introduction
    print("Spyware Health:", spyware_health)
    print(name, "Health:", character_health)

    while spyware_health > 0 and character_alive == True:
      print("")
      print("What will you do?")
      print("")
      print("A) Close ranged  (s:", strength - 1, ") (r:", reliability - 2,")")
      print("B) Ranged attack (s:", strength - 3, ") (r:", reliability, ")")
      print("C) Use Firewall count:", firewall)
      print("")
      move = input("Move: ")
      print("")

      #User correct statemnt
      while move != "A" and move != "B" and move != "C":
        print("Please choose a given prompt above.")
        move = input("Move: ")
        print("")

      #Closed range attack chances
      if move == "A":
        roll = random.randint(0,10)
        if roll <= c_r_r:
          print("You hit Spyware with a close ranged attack!")
          spyware_health = spyware_health - c_r_s
          print("Spyware Health:", spyware_health, "/ 35")
          print("")
          if spyware_health >= 0: 
            print("Spyware attacks!")
            print("")
            enemy_roll = random.randint(0,10)
            if enemy_roll <= 8 - speed:
              print("Spyware hit you!")
              character_health = character_health - 9
              print("Your health:", character_health, "/ 50")
              if character_health <= 0:
                print("")
                print("You have died")
                character_alive = False

            #Miss statement
            else:
              if spyware_health >= 0:
                print("Spyware missed!")
          
          #If the boss dies, award the player
          else:
            print("Spyware has been defeated!")
            print("Your speed was increased by +2!")
            speed = speed + 2

        #User misses attack
        else:
            print("You missed your close ranged attack!")
            print("")
            print("Spyware attacks!")
            print("")
            enemy_roll = random.randint(0,10)
            if enemy_roll <= 8 - speed:
              print("Spyware hit you!")
              character_health = character_health - 8
              print("Your health:", character_health, "/ 50")
              if character_health <= 0:
                print("")
                print("You have died")
                character_alive = False
            else:
              if spyware_health >= 0:
                print("Spyware missed!")

      #Ranged attack chances
      elif move == "B":
        roll = random.randint(0,10)
        if roll <= r_a_r:
          print("You hit Spyware with a ranged attack!")
          spyware_health = spyware_health - r_a_s
          print("Spyware Health:", spyware_health, "/ 35")
          print("")
          if spyware_health > 0: 
            print("Spyware attacks!")
            print("")
            enemy_roll = random.randint(0,10)
            if enemy_roll <= 7 - speed:
              print("Spyware hit you!")
              character_health = character_health - 7
              print("Your health:", character_health, "/ 50")
              if character_health <= 0:
                print("")
                print("You have died")
                character_alive = False
            
            #Enemy misses
            else:
              if spyware_health >= 0:
                print("Spyware missed!")

          #If spyware dies this plays
          else:
            print("Spyware has been defeated!")
            print("Your speed has increased by +2!")
            speed = speed + 2

        #If you miss your ranged attack
        else:
            print("You missed your ranged attack!")
            print("")
            print("Spyware attacks!")
            print("")
            enemy_roll = random.randint(0,10)
            if enemy_roll <= 7 - speed:
              print("Spyware hit you!")
              character_health = character_health - 6
              print("Your health:", character_health, "/ 50")
              if character_health <= 0:
                print("")
                print("You have died")
                character_alive = False
            else:
              if spyware_health >= 0:
                print("Spyware missed!")

      #Health regeneration calculations
      else:
        if move == "C":
          if firewall >= 1:
            firewall = firewall - 1
            if character_health >= 25:
              character_health = 50
              print("FIREWALL CONSUMED")
              print(name, "Health:", character_health)

            else:
              character_health = character_health + 25
              print("FIREWALL CONSUMED")
              print(name, "Health:", character_health)
            
          else:
            print("You have no more Firewalls!")

  #Sneak scenario with a guessing game
  else:
    if choice == "sneak":
      print("You see a safe in the far corner of the room.")
      print("You have three attempts to guess the number to unlock it.")
      safe = random.randint(1,5)
      print("")
      print("Guess a number from 1-5")
      guess = int(input("Your guess: "))

      #Variable set up
      guess_left = 3
      open_safe = False

      #User corrections
      while guess != 1 and guess != 2 and guess != 3 and guess != 4 and guess != 5:
        print("")
        print("Please type a number from 1-5")
        guess = int(input("Your guess: "))

      #If the guess isn't correct
      while guess != safe and guess_left > 1:
        guess_left = guess_left - 1
        print("")
        print("*Nothing happens*")
        print(guess_left, "/ 3")
        guess = int(input("Your guess: "))

      #If the guess is right
      if guess == safe:
        print("")
        print("*You hear a click*")
        print("*The safe door swings open*")
        print("Your firewall count has increased by +1!")
        print("")
        input("Press enter to continue: ")
        open_safe = True

      #If the user doesn't open the safe they have to fight
      if open_safe == False:
        print("")
        print("You ran out of attempts.")
        print("The safe locks you out and signals and alarm")
        print("")
        input("Press enter to continue: ")

        character_health = 50
        spyware_health = 35

        #Updates stats with any new relics or upgrades
        c_r_s = strength - 1
        c_r_r = reliability - 2

        r_a_s = strength - 3
        r_a_r = reliability

        #Firewall calculations
        if fight_1 == True:
          firewall = 3
        else:
          firewall = 2
        
        #Fight introduction
        print("")
        print("Spyware Health:", spyware_health)
        print(name, "Health:", character_health)

        while spyware_health > 0 and character_alive == True:
          print("")
          print("What will you do?")
          print("")
          print("A) Close ranged  (s:", strength - 1, ") (r:", reliability - 2,")")
          print("B) Ranged attack (s:", strength - 3, ") (r:", reliability, ")")
          print("C) Use Firewall count:", firewall)
          print("")
          move = input("Move: ")
          print("")

          #User correct statemnt
          while move != "A" and move != "B" and move != "C":
            print("Please choose a given prompt above.")
            move = input("Move: ")
            print("")

          #Closed range attack chances
          if move == "A":
            roll = random.randint(0,10)
            if roll <= c_r_r:
              print("You hit Spyware with a close ranged attack!")
              spyware_health = spyware_health - c_r_s
              print("Spyware Health:", spyware_health, "/ 35")
              print("")
              if spyware_health >= 0: 
                print("Spyware attacks!")
                print("")
                enemy_roll = random.randint(0,10)
                if enemy_roll <= 8 - speed:
                  print("Spyware hit you!")
                  character_health = character_health - 9
                  print("Your health:", character_health, "/ 50")
                  if character_health <= 0:
                    print("")
                    print("You have died")
                    character_alive = False

                #If enemy miss
                else:
                  if spyware_health >= 0:
                    print("Spyware missed!")
              else:
                print("Spyware has been defeated!")
                print("Your speed has increased by +2!")
                speed = speed + 2

            #If the user misses the hit
            else:
                print("You missed your close ranged attack!")
                print("")
                print("Spyware attacks!")
                print("")
                enemy_roll = random.randint(0,10)
                if enemy_roll <= 8 - speed:
                  print("Spyware hit you!")
                  character_health = character_health - 8
                  print("Your health:", character_health, "/ 50")
                  if character_health <= 0:
                    print("")
                    print("You have died")
                    character_alive = False
                else:
                  print("Spyware missed!")

          #Ranged attack chances
          elif move == "B":
            roll = random.randint(0,10)
            if roll <= r_a_r:
              print("You hit Spyware with a ranged attack!")
              spyware_health = spyware_health - r_a_s
              print("Spyware Health:", spyware_health, "/ 35")
              print("")
              if spyware_health > 0:
                print("Spyware attacks!")
                print("")
                enemy_roll = random.randint(0,10)
                if enemy_roll <= 7 - speed:
                  print("Spyware hit you!")
                  character_health = character_health - 7
                  print("Your health:", character_health, "/ 50")
                  if character_health <= 0:
                    print("")
                    print("You have died")
                    character_alive = False
                else:
                  if spyware_health >= 0:
                    print("Spyware missed!")
              else:
                print("Spyware has been defeated!")
                print("Your speed was increased by +2!")
                speed = speed + 2

            #If the user misses the close ranged attack
            else:
                print("You missed your ranged attack!")
                print("")
                print("Spyware attacks!")
                print("")
                enemy_roll = random.randint(0,10)
                if enemy_roll <= 7 - speed:
                  print("Spyware hit you!")
                  character_health = character_health - 6
                  print("Your health:", character_health, "/ 50")
                  if character_health <= 0:
                    print("")
                    print("You have died")
                    character_alive = False
                else:
                  print("Spyware missed!")

          #Health regeneration calculations
          else:
            if move == "C":
              if firewall >= 1:
                firewall = firewall - 1
                if character_health >= 25:
                  character_health = 50
                  print("FIREWALL CONSUMED")
                  print(name, "Health:", character_health)

                else:
                  character_health = character_health + 25
                  print("FIREWALL CONSUMED")
                  print(name, "Health:", character_health)
                
              else:
                print("You have no more Firewalls!")

#Treasury path
else:
  choice == "treasury"
  print("")
  print("You see a safe in the far corner of the room.")
  print("You have three attempts to guess the number to unlock it.")
  safe = random.randint(1,5)
  print("")

  #User input
  print("Guess a number from 1-5")
  guess = int(input("Your guess: "))

  #Variable set up
  guess_left = 3
  open_safe = False

  #If the guess is incorrect
  while guess != 1 and guess != 2 and guess != 3 and guess != 4 and guess != 5:
    print("")
    print("Please type a number from 1-5")
    guess = int(input("Your guess: "))

  #If the guess is wrong
  while guess != safe and guess_left > 0:
    guess_left = guess_left - 1
    print("")
    print("*Nothing happens*")
    print(guess_left, "/ 3")
    guess = int(input("Your guess: "))

  #If the guess is right
  if guess == safe:
    print("*You hear a click*")
    print("*The safe door swings open*")
    print("Your reliability has just increased by +2!")
    reliability = reliability + 2
    open_safe = True

  #If the user doesn't open the safe they have to fight
  if guess_left == 0 and open_safe == False:
    print("You ran out of attempts.")
    print("*The safe locks you out*")

#Adventure text
print("")
input("Press enter to continue: ")
print("")
print("*You wander around the rest of the area*")
print("")
print("*You arrive at an empty cave with many giant holes in the wall*")
print("")
input("Enter space to continue: ")
print("")
print("*You feel tremors from deep within the holes in the wall*")
print("")
input("Enter to continue: ")
print("")
print("Mydoom, the great worm, has appeared!")
print("")

#Variable set up
f_fight = True
character_health = 50
mydoom_health = 65

#Updates stats with any new relics or upgrades
c_r_s = strength - 1
c_r_r = reliability - 2

r_a_s = strength - 3
r_a_r = reliability

#Firewall set up
firewall = 2

if fight_1 == True:
  firewall = firewall + 1

if open_safe == True:
  firewall = firewall + 1

#Fight: Final boss
if f_fight == True:
  print("Mydoom Health:", mydoom_health)
  print(name, "Health:", character_health)
  while mydoom_health > 0 and character_alive == True:
    print("")
    print("What will you do?")
    print("")
    print("A) Close ranged  (s:", strength - 1, ") (r:", reliability - 2,")")
    print("B) Ranged attack (s:", strength - 3, ") (r:", reliability, ")")
    print("C) Use Firewall count:", firewall)
    print("")
    move = input("Move: ")
    print("")

    #User correct statemnt
    while move != "A" and move != "B" and move != "C":
      print("Please choose a given prompt above.")
      move = input("Move: ")
      print("")

    #Closed range attack chances
    if move == "A":
      roll = random.randint(0,10)
      if roll <= c_r_r:
        print("You hit Mydoom with a close ranged attack!")
        mydoom_health = mydoom_health - c_r_s
        print("MyDoom Health:", mydoom_health, "/ 65")
        print("")
        if mydoom_health >= 0: 
          print("Mydoom attacks!")
          print("")
          enemy_roll = random.randint(0,10)
          if enemy_roll <= 11 - speed:
            print("Mydoom hit you!")
            character_health = character_health - 12
            print("Your health:", character_health, "/ 50")
            if character_health <= 0:
              print("")
              print("You have died")
              character_alive = False

          else:
            if mydoom_health >= 0:
              print("Mydoom missed!")
        else:
          print("Mydoom has been defeated!")
          input("Press enter to continue: ")

      else:
          print("You missed your close ranged attack!")
          print("")
          print("Mydoom attacks!")
          print("")
          enemy_roll = random.randint(0,10)
          if enemy_roll <= 11 - speed:
            print("Mydoom hit you!")
            character_health = character_health - 12
            print("Your health:", character_health, "/ 50")
            if character_health <= 0:
              print("")
              print("You have died")
              character_alive = False
          else:
            if mydoom_health >= 0:
              print("Mydoom missed!")

    #Ranged attack chances
    elif move == "B":
      roll = random.randint(0,10)
      if roll <= r_a_r:
        print("You hit Mydoom with a ranged attack!")
        mydoom_health = mydoom_health - r_a_s
        print("Mydoom Health:", mydoom_health, "/ 65")
        print("")
        if mydoom_health > 0: 
          print("Mydoom attacks!")
          print("")
          enemy_roll = random.randint(0,10)
          if enemy_roll <= 10 - speed:
            print("Mydoom hit you!")
            character_health = character_health - 10
            print("Your health:", character_health, "/ 50")
            if character_health <= 0:
              print("")
              print("You have died")
              character_alive = False
          else:
            if mydoom_health >= 0:
              print("Mydoom missed!")
        else:
          print("Mydoom has been defeated!")
          input("Press enter to continue: ")

      else:
          print("You missed your ranged attack!")
          print("")
          print("Mydoom attacks!")
          print("")
          enemy_roll = random.randint(0,10)
          if enemy_roll <= 10 - speed:
            print("Mydoom hit you!")
            character_health = character_health - 10
            print("Your health:", character_health, "/ 50")
            if character_health <= 0:
              print("")
              print("You have died")
              character_alive = False
          else:
            if mydoom_health >= 0:
              print("Mydoom missed!")

    #Health regeneration calculations
    else:
      if move == "C":
        if firewall >= 1:
          firewall = firewall - 1
          if character_health >= 25:
            character_health = 50
            print("FIREWALL CONSUMED")
            print(name, "Health:", character_health)

          else:
            character_health = character_health + 25
            print("FIREWALL CONSUMED")
            print(name, "Health:", character_health)
          
        else:
           print("You have no more Firewalls!")

#End game interactions

if character_alive == True:
  print("")
  print("Congradulations!")
  print("")
  print("You have defeated the viruses infecting this computer!")
  print("Finally, to leave Jumanji you must type it out in all capital letters!")
  print("")
  end_inp = input("")

  while end_inp != "JUMANJI":
    print("")
    print("Aw come on... try again")
    end_inp = input("")

  if end_inp == "JUMANJI":
    print("")
    print("The end")
    print("Thank you for playing!")