import random

def number2name(number):
    """convert number to name"""
    if number==0:
        return "rock"
    elif number==1:
        return "spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    else:
        return "scissors"

def name2number(name):
    """convert name to number"""
    if name=="rock":
        return 0
    elif name=="spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    else:
        return 4

def rpsls(name):
    """to calculate who is the winner of the game"""
    player=name2number(name)
    computer=random.randrange(0,4)
    print "Player choose",name
    print "Computer choose",number2name(computer)
    cond=(computer-player) % 5
    if player==computer:
        print "Computer and player choose the same one"
    if cond<3:
        print "Computer wins!\n\n"
    else:
        print "Player wins!\n\n"

rpsls("rock")
rpsls("scissors")
rpsls("spock")
    
