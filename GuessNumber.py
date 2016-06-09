import simplegui
import random

rightnumber=0
count=0

def range100():
    global rightnumber,count
    rightnumber=random.randrange(1,100)
    count=7
    print "New game, Range is from 0 to 100"
    print "Numeber of remaining guesses is",count
    print ""
    return
    
def range1000():
    global rightnumber,count
    rightnumber=random.randrange(1,1000)
    count=9
    print "New game, Range is from 0 to 1000"
    print "Number of remaining guesses is",count
    print ""
    return

def get_input(guess):
    global count
    if rightnumber!=0:
        number=int(guess)
        count-=1
        print "Guess is",number
        print "Number of remaining guesses is",count
        if number==rightnumber:
            print "Correct"
        elif number>rightnumber:
            print "Lower"
        else:
            print "Higher"
        print ""
    else:
        return 



frame=simplegui.create_frame("Guess number",200,200)
frame.add_button("Range100",range100,100)
frame.add_button("Range1000",range1000,100)
guess=frame.add_input("Enter number",get_input,100)
