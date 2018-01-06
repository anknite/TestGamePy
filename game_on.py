
def SphinxHall(usr,health,coins):
    if health == 0:
        dead()

    print "\n"
    print "You have entered the Sphinx Hall, The Sphinx is guarding the Door."
    print "The Sphinx askes you a question."
    print "Answer the Sphinx's question ?"
    print "1. Yes \n or press any character to skip the Sphinx."
    choice = raw_input("-> ")
    if choice == "1":
        print "How much is 4 times 3 minus 10 ?"
        ans = raw_input("=> ")
        if ans == "2":
           print "\n"
           print "Correct !! The Sphinx is Happy. It rewards you with 200 gold coins"
           print "The Sphinx has opened the door for you!!."
           coins += 200
           TreasureCastle(usr,health,coins);
        else:
           print "\n"
           print "Wrong !! Sphinx is angry with you. Get out of there."
           print "1 . Yes \n 2. No"
           out = raw_input("=> ")
           if out == "1":
              TreasureCastle(usr,health,coins)
           elif out == "2":
              print "\n"
              print "You are brave but the Sphinx has hit you hard."
              dead()

           else:
              print "\n"
              print " Please enter a correct choice \"1\" or \"2\""
              SphinxHall(usr,health,coins)
    else:
        print "\n"
        print "You have skiped the Sphinx's question. You can go through the Door"
        TreasureCastle(usr,health,coins) 


def TreasureCastle(usr,health,coins):
    print " Well done "+usr+" !!\n"
    print usr
    print health
    print coins
    print "You have successfully completed Treasure Castle with "+str(coins)+" gold coins and "+str(health)+"% health remaining :)"
    print "We will get back to you with more amazing adventures.. \n\n"
    print " Credits: Python, Linux and @anknite :)"     
    exit(1)

def dead():
     print "Lost all your health."
     print "You are Dead. Game Over !!"
     exit(0)

def DragonLair(usr,health,coins):
    if health == 0:
       dead()
    print "\n"
    print "You have entered the Dragon's Lair, Its better to get out of here quickly."
    print "There are 3 doors. 1 on your left , 1 on right and 1 straight ahead:"
    print "Choose: "
    print "1. Open Door on left."
    print "2. Open Door on your Right."
    print "3. Open Door in front of you."
 
    opt2 = raw_input("=> ")
    if opt2 =="1":
        print "\n"
        print "Ohh, there is a hound inside, It attackes you loose 25% of your Health"
        health -= 25
        DragonLair(usr,health,coins)
    elif opt2 == "2":
        print "\n"
        print "Wow ! you escaped the Dragon's lair."
        print "Lucky you!!"
        SphinxHall(usr,health,coins)

    elif opt2 == "3":
        print "\n"
        print "Oh my God ! Thats the angry Dragon, It has burnt you with its fire.."
        dead() 
    else:
        print "\n"
        print " Please enter a correct choice \"1\" or \"2\" or \"3\""
        DragonLair(usr,health,coins)
       
     

def game(usr):
    health = 100
    counter = 0
    coins = 0
    print "Enter the Treasure Castle\n 1.yes \n 2.no !!"
    open = raw_input("-> ")
    
    if open == "1":
        enter_castle(usr,health,coins,counter)
    elif open == '2':
        print "No Problem !! you can always come back and play. Have a nice day!!"
    else:
        print "\n"
        print " Please enter a correct choice \"1\" or \"2\""
        game(usr)

def enter_castle(usr,health,coins,counter):     
    if health <= 0:
        dead()
    print "\n"
    print "There's a sleeping hound on your right, Door 1 on your left and Door 2 straight"
    print "Choose: "
    print "1. Disturb the Hound."
    print "2. Open Door 2 on your left."
    print "3. Open Door 3 in front of you."
    
    opt1 = raw_input("=> ")
    if opt1 =="1":
        print "\n"
        print "The Hound is angry, It attacked you. You loose 25 % of your health."
        health -= 25
        enter_castle(usr,health,coins,counter)
            
    elif opt1 == "2":
        if counter > 3:
            health -= 50
            print "You are greedy, the guardian snake has bit you. You loose 50 % of your health"  
        else:
            print "\n"
            print "Ahh you have found the Magic Door, The guardian snake gives you 100 gold coins"
            coins += 100
            counter += 1

        enter_castle(usr,health,coins,counter)
        
    elif opt1 == "3":
        DragonLair(usr,health,coins)
        #if health == 0:
        #  dead()
    else:
        print "\n"
        print " Please enter a correct choice \"1\" or \"2\" or \"3\""
        enter_castle(usr,health,coins,counter)
    
def hello(usr):
    print "Welcome "+usr
    print " This is TREASURE CASTLE !!!! "
    print "Loading ...."
    print "Game Begins !!!!"
    game(usr) 

usr = raw_input("Enter your name: ")
if usr =="":
   usr = "Anonymous User"
hello(usr)
