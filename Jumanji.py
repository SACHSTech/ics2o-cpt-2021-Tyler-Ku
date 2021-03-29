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

char = (0)
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
  print("Strength:", strength, "    (Attack damage)")
  print("Speed:", speed, "       (Chance to dodge enemy attack) ")
  print("Reliability:", reliability, " (Chance to hit your attack) ")

elif char == 2:
  strength = 9
  speed = 3
  reliability = 6
  print("Strength:", strength, "    (Attack damage)")
  print("Speed:", speed, "       (Chance to dodge enemy attack) ")
  print("Reliability:", reliability, " (Chance to hit your attack) ")
  
elif char == 3:
  strength = 5
  speed = 5
  reliability = 8
  print("Strength:", strength, "    (Attack damage)")
  print("Speed:", speed, "       (Chance to dodge enemy attack) ")
  print("Reliability:", reliability, " (Chance to hit your attack) ")

else:
  strength = 9
  speed = 3
  reliability = 6
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
print("You come across a path splitting two ways. Do you go left or right?")

fight_1 = True
path_1 = ""

choice_1 = input("Where do you choose?: ")

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

character_health = 50
adware_health = 10

c_r_s = strength - 1
c_r_r = reliability - 2

r_a_s = strength - 3
r_a_r = reliability

firewall = 2

if fight_1 == True:
  print("You come upon your first enemy.")
  print("Adware Health:", adware_health)
  print(name, "Health:", character_health)
  while adware_health >= 0:
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
          if enemy_roll <= 3:
            print("Adware hit you!")
            character_health = character_health - 5
            print("Your health:", character_health)
          else:
            if adware_health >= 0:
              print("Adware missed!")
        else:
          print("Adware has been defeated!")
          input("Press enter to continue: ")

      else:
          print("You missed your close ranged attack!")
          print("")
          print("Adware attacks!")
          print("")
          enemy_roll = random.randint(0,10)
          if enemy_roll <= 3:
            print("Adware hit you!")
            character_health = character_health - 5
            print("Your health:", character_health)
          else:
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
          if enemy_roll <= 3:
            print("Adware hit you!")
            character_health = character_health - 5
            print("Your health:", character_health)
          else:
            if adware_health >= 0:
              print("Adware missed!")
        else:
          print("Adware has been defeated!")
          input("Press enter to continue: ")

      else:
          print("You missed your ranged attack!")
          print("")
          print("Adware attacks!")
          print("")
          enemy_roll = random.randint(0,10)
          if enemy_roll <= 3:
            print("Adware hit you!")
            character_health = character_health - 5
            print("Your health:", character_health, "/ 50")
          else:
            print("Adware missed!")

    #Health regeneration calculations
    else:
      if move == "C":
        firewall = firewall - 1
        if character_health >= 25:
          character_health = 50
        else:
          character_health = character_health + 25
        print("FIREWALL CONSUMED")
        print(name, "Health:", character_health)

else:
  print("This path seems empty and arid.")

#Questionare
print("")
print("You come across a giant door with enscribed words.")
print('It says, "To open the door you must answer the following question"')
print("")
print('"Which of the following is a famous example of Ransomware?"')
print("")
print("A) SadBoy")
print("B) tREX")
print("C) GoldenWind")
print("D) WannaCry")
print("")
choice = input("Your answer: ")
print("")

fight_2 = True

while choice != "A" and choice != "B" and choice != "C" and choice != "D":
  print("Please choose a valid answer")
  choice = input("Your answer: ")

if choice == "D":
  print("Correct answer")
  fight_2 = False

else:
  print("Incorrect answer")
  print("*You hear rumbling from above*")
  print("")
  input("Press enter to continue: ")
  print("")
  print("A browser highjacker appears!")

character_health = 50
browser_health = 25
firewall = 2
character_alive = True

#Fight 2
if fight_2 == True:
  print("Browser highjacker Health:", browser_health)
  print(name, "Health:", character_health)
  while browser_health >= 0 and character_alive == True:
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
          if enemy_roll <= 5:
            print("Browser highjacker hit you!")
            character_health = character_health - 8
            print("Your health:", character_health)
            if character_health <= 0:
              print("")
              print("You have died")
              character_alive = False

          else:
            if adware_health >= 0:
              print("Browser highjacker missed!")
        else:
          print("The Browser highjacker has been defeated!")
          input("Press enter to continue: ")

      else:
          print("You missed your close ranged attack!")
          print("")
          print("Browser highjacker attacks!")
          print("")
          enemy_roll = random.randint(0,10)
          if enemy_roll <= 5:
            print("Browser highjacker hit you!")
            character_health = character_health - 8
            print("Your health:", character_health)
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
          if enemy_roll <= 5:
            print("Browser highjacker hit you!")
            character_health = character_health - 8
            print("Your health:", character_health)
            if character_health <= 0:
              print("")
              print("You have died")
              character_alive = False
          else:
            if adware_health >= 0:
              print("Browser highjacker missed!")
        else:
          print("The Browser highjacker has been defeated!")
          input("Press enter to continue: ")

      else:
          print("You missed your ranged attack!")
          print("")
          print("Browser highjacker attacks!")
          print("")
          enemy_roll = random.randint(0,10)
          if enemy_roll <= 5:
            print("Browser highjacker hit you!")
            character_health = character_health - 8
            print("Your health:", character_health, "/ 50")
            if character_health <= 0:
              print("")
              print("You have died")
              character_alive = False
          else:
            print("Browser highjacker missed!")

    #Health regeneration calculations
    else:
      if move == "C":
        firewall = firewall - 1
        if character_health >= 25:
          character_health = 50
        else:
          character_health = character_health + 25
        print("FIREWALL CONSUMED")
        print(name, "Health:", character_health)

print("The door rumbles and opens to a long hallway")
print("")

#print(random.randint(0,10))