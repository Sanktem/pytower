# This is going to be a really crappily designed idle game tbh

# Modules
import random
from time import sleep
from os import system, name

#global vars
gold = 1
max_health = 10
curr_health = 10
attack = 3
max_mana = 10
curr_mana = 10
level = 1
intel = 3
luck = 1
speed = 3
crit_chance = 1
crit_strike = 1
wisdom = 3
curr_floor = 1
player_name = 'NA'
gender = 'NA'
null = '0'

#lists
numbers = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
stats = [ gold, max_health, max_mana, curr_health, curr_mana, level, attack, intel, luck, speed, crit_chance, crit_strike, wisdom, player_name, gender, curr_floor, null ]

#Creation of the character! This will be before the main menu and not able to be returned to
def create():
    global gold, max_health, max_mana, curr_health, curr_mana, level, attack, intel, luck, speed, crit_chance, crit_strike, wisdom, player_name, gender, curr_floor, null, major, minor, major_pick
    choice = 0
    difficulty = 0
    major = 0
    minor = 0
    null = 0
    
    clear()
    print('Hello and welcome to the never ending tower of Doom.... I kid, but really it is dangrous, if you die on this tower, then you are done for good there are no secound chances in this tower. The higer in the tower that you manage the more money, riches, and other wonderful tresures will be yours, but you have to fight for it. This will be your greatest challenge in your life. Will you take the challenge or will you give up before even starting.')
    pause() # ^^ Opening statement to the game I guess 
    
    player_name = str(input(' What is your name?    ')) # Changes everything but luck
    gender = str(input(' What is your gender?    ')) # Changes total luck
    
    while difficulty  == 0 or difficulty < 1 or difficulty > 10: # Checks and makes sure the this number is an interger
        try:
            difficulty = int(input(' From a scale from 1-10 how much do you hate yourself?  ')) # Height of the tower difficulty * 10
            if difficulty < 1 or difficulty > 10: # Confirms the vlaues is within range
                print(' That is not within the correct range')
                sleep(1)
            else:
                pass
        except ValueError:
            print(' Only a number will do')
            sleep(1)
        
    print('\n Thank you your input will change how the game is played\n \n The next step is that we are going to chose the focuse areas of your character, there are no classes, because I have no idea of what I want to do with those yet') 
    pause()
    clear()

    print('\nThis is how it is going to work, you are going to pick a major and minor stat this will give thoes stats a higher chance to grow per level that you gain. Finally you can also pick a null stat this will stop this stat from growing but give major stat a 100% chance to increase every level')
    try:
        null_choice = int(input( '\n Would you like to use a null stat 1-Yes 0-No: '))
        if null_choice == 1:
            while True:
                clear()
                print_stats()
                try:
                    stat_choice = int(input('\n What stat do you just not care about? (You can not Null out health yet.....): '))
                    if stat_choice == 1: #Health
                        print('Nope you can not null out health yet')
                        sleep(1)
                    elif stat_choice == 2: #Mana
                        max_mana = 0
                        curr_mana = 0
                        null = 'Mana'
                        print(' It is done your Mana will be 0')
                        break
                    elif stat_choice == 3: #Attack
                        attack = 0
                        null = 'Attack'
                        print(' It is done your Strength will be 0')
                        break
                    elif stat_choice == 4: #Speed
                        speed = 0
                        null = 'Speed'
                        print(' It is done your Aglity will be 0')
                        break
                    elif stat_choice == 5: #Intelligance
                        intel = 0
                        null = 'Intelligance'
                        print(' It is done your Intelligance will be 0')
                        break
                    elif stat_choice == 6: #Wisdom
                        wisdom = 0
                        null = 'Wisdom'
                        print(' It is done your Wisdom will be 0')
                        break
                    elif stat_choice == 7: #Critical Chance
                        crit_chance = 0
                        null = 'Critical Chance'
                        print(' It is done your Critical Chance will be 0')
                        break
                    elif stat_choice == 8: #Critical Strike
                        crit_strike = 0
                        null = 'Critical Strike'
                        print(' It is done your Critical Strike will be 0')
                        break
                    elif stat_choice == 9: #Luck
                        luck = 0
                        null = 'Luck'
                        print(' It is done your Luck will be 0')
                        break
                    else:
                        print(' That is not a valid option')
                        sleep(1)
                except ValueError:
                    print(' Only a number will do')
            pause()        
        elif null_choice == 0:
            print(' Cool moving on to picking your major and minor stats')
        else:
            print(' That is not a valid option')
            sleep(1)
    except ValueError:
        print(' Only a number will do')
        sleep(1)
    
    pause() # This will allow the player to select the Major stat
    clear()
    print('\n For your Major stat you will start with 2 extra bonus points and a 66% chance that you will level up in that stat. For your minor stat you will start with one extra point and a 40% to earn a point every level. For all other stats you will have a 15% to gain a point in any of the remaining skills. \n Note: If you have a null stat then you will have a 100% chance to gain a point in your major stat. \n \n')
    print_stats()
    while True:
        try: 
            major_choice = int(input('What do you want your major stat to be?: ')
            if major_choice == 1: #Health
                if_null('Health')
                max_health = 12
                curr_health = max_health
                major = 'Health'
                print('Your total health has been set to:', max_health)
                break
            elif major_choice == 2: #Mana
                if_null('Mana')
                max_mana = 12
                curr_mana = max_mana
                major = 'Mana'
                print('Your total mana has been set to:', max_mana)
                break
            elif major_choice == 3: #Attack
                if_null('Attack')
                attack = 5
                major = 'Attack'
                print('Your strength has been set to:', attack)
                break
            elif major_choice == 4: #Speed
                if_null('Speed')
                speed = 5
                major = 'Speed'
                print('Your aglity has been set to:', speed)
                break
            elif major_choice == 5: #Intelligance
                if_null('Intelligance')
                intel = 5
                major = 'Intelligance'
                print('Your intelligance has been set to:', intel)
                break
            elif major_choice == 6: #Wisdom
                if_null('Wisdom')
                wisdom = 5
                major = 'Wisdom'
                print('Your wisdom has been set to:', wisdom)
                break
            elif major_choice == 7: #Critical Chance
                if_null('Critical Chance')
                crit_chance = 3
                major = 'Critical Chance'
                print('Your criical chance has been set to:', crit_chance)
                break
            elif major_choice == 8: #Critical Strike
                if_null('Critical Strike')
                crit_strike = 3
                major = 'Critical Strike'
                print('Your critical strike has been set to:', crit_strike)
                break
            elif major_choice == 9: #Luck
                if_null('Luck')
                luck = 3
                major = 'Luck'
                print('Your luck has been set to:', luck)
                break
            else:
                print(' That is not a valid option')
                sleep(1)
        except ValueError:
            print(' Only a number will do')
    pause()
        
    
#Main menu
def main():
    global gold, curr_floor
    choice = 0
    
    while choice == 0: # While loop will reset when the main function is called again. This is correct for incorrect inputs
        clear()
        print('\n Welcome to the main menu! The following are your options\n \n 1-See Character Info\n 2-Attack a New Monster\n 3-Inventory\n 4-Blacksmith\n 5-Item Merchant\n 6-Go up a floor\n 7-Leave the Tower')
        basestats()
        try:
            choice = int(input('\n What would you like to do?: '))
            if choice == 1: # This statment will move the players choice on to the correct function
                stats()
            elif choice == 2:
                mon1()
            elif choice == 3:
                inventory()
            elif choice == 4:
                blacksmith()
            elif choice == 5:
                itmm()
            elif choice == 6:
                floor()
            elif choice == 7:
                exit()
            else:
                print('You did not enter a valid option')
                sleep(1)
        except ValueError:
            print('You did not enter a valid option')
            sleep(1)

# Base stats, this is to show basic vlaues like current health, and mana and attack
def basestats():
    global gold, max_health, max_mana, curr_health, curr_mana, level, curr_floor, stats
    print('\n You are currently level', level, '\n Your current health is', curr_health, '/', max_health, '\n Your current mana is', curr_mana, '/', max_mana)
    print('\n You currently have: ', gold, 'gold.')
    print(' You are currently on floor: ', curr_floor)
    
  
#Stats, shows the stats for the character that you have farther then basic stats shown in the welcome screen
def stats():
    global gold, max_health, max_mana, curr_health, curr_mana, level, attack, intel, luck, speed, crit_chance, crit_strike, wisdom, null, major, minor, player_name, gender, curr_floor
    clear()
    print('\n Hello,' player_name, ' with the you are the gender of', gender)
    print('\n This is your current stats!')
    print('\n You are currently level', level, '\n Your current health is', curr_health, '/', max_health, '\n Your current mana is', curr_mana, '/', max_mana)
    print('\n You currently have,', gold, 'gold.')
    print(' You are currently on floor: ', curr_floor)
    print('\n Other stats')
    print('\n Strength:        ', attack, '\n Aglity:          ', speed, '\n Intelligance:    ', intel, '\n Wisdom:          ', wisdom, '\n Critical chance: ', crit_chance, '\n Critical Strike: ', crit_strike, '\n Luck:            ', luck)
    if null != '0':
        print ('\n Your major stat is', major, '\n Your minor stat is', minor, '\n Your null stat is', null)
    else:
        print ('\n Your major stat is', major, '\n Your minor stat is', minor)
    pause()
    
    main()
    
#Monster rng 1 basic easy grunt monster
def mon1():
    print('\n mon1 \n')
#Monster rng 2 medium monster
def mon2():
    print('\n mon2 \n')
#Monster rng 3 mini boss level monsters.
#You will have to add more functions for the other monsters to change the diffrent move pools, but that is for a later time
def mon3():
    print('\n mon3 \n')
#Blacksmith alloes the crafting of basic items
def blacksmith():
    print('\n blacksmith \n')
#Item Merchant buying assorricies/potions, and other crafting materials
def itmm():
    print('\n itmm \n')
#Function to go up a floor will check if you are high enough level/fought enought monsters
def floor():
    print('\n floor \n')
#Looking at and managing the inventory of the player
def inventory():
    print('\n This is what is currently in your bag\n')
    
#Clear the screan function to make the program look cleaner
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
#Pause and wait until player input 
def pause():
    programPause = input("\n Press the <ENTER> key to continue...")

# Im lazy and this is in my program like 3 times
def print_stats():
    print('\n You have the following stats, \n \n 1-Health \n 2-Mana \n 3-Strength \n 4-Aglity \n 5-Intelligance \n 6-Wisdom \n 7-Critical Chance \n 8-Critical Strike \n 9-Luck')

#Will check if the stat is null stat
def if_null(major_pick):
    global gold, max_health, max_mana, curr_health, curr_mana, level, attack, intel, luck, speed, crit_chance, crit_strike, wisdom, null, major, minor, player_name, gender, curr_floor, major_pick
    if null == major_pick: 
        print('\n This is the null stat please pick another')
    else:
        pass

create()
main()