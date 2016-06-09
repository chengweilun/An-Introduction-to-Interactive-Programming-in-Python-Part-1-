#Implementation of classic arcade game Pong

import simplegui
import random

#initialize global - pos and vel encode vertical info for paddled
WIDTH=600
HEIGHT=400
BALL_RADIUS=10
PAD_WIDTH=8
PAD_HEIGHT=80
HALF_PAD_WIDTH=PAD_WIDTH/2
HALF_PAD_HEIGHT=PAD_HEIGHT/2
LEFT=False
RIGHT=True
vel=4
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[0,0]
paddle1_pos=[PAD_WIDTH/2,HEIGHT/2]
paddle2_pos=[WIDTH-PAD_WIDTH/2,HEIGHT/2]
paddle1_vel=paddle2_vel=0

#initialize ball_pos and ball_vel for new bal in middle of table
#if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos,ball_vel  #these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2]  
    if direction==True:
        ball_vel=[1,-1]
    if direction==False:
        ball_vel=[-1,-1]
    timer.start()
        
#define event handlers
def new_game():
    global paddle1_pos,paddle2_pos,paddle1_vel,paddle2_vel  #these are numbers
    global score1,score2   #these are ints
    paddle1_pos=[PAD_WIDTH/2,HEIGHT/2]
    paddle2_pos=[WIDTH-PAD_WIDTH/2,HEIGHT/2]
    paddle1_vel=paddle2_vel=0
    score1=score2=0
    spawn_ball(RIGHT)
    
def draw(c):
    global score1,score2,paddle1_pos,paddle2_pos,ball_pos,bell_vel
    #draw mid line and gutters
    c.draw_line([WIDTH/2,0],[WIDTH/2,0],1,"whith")
    c.draw_line([PAD_WIDTH,0],[PAD_WIDTH,HEIGHT],1,"White")
    c.draw_line([WIDTH-PAD_WIDTH,0],[WIDTH-PAD_WIDTH,HEIGHT],1,"white")
    
    #update ball
    
    if ball_pos[1]<=BALL_RADIUS or ball_pos[1]>=HEIGHT-BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
    
    if ball_pos[0]<=(PAD_WIDTH+BALL_RADIUS):
        if (ball_pos[1]<=(paddle1_pos[1]-PAD_HEIGHT/2)) or  (ball_pos[1]>=(paddle1_pos[1]+PAD_HEIGHT/2)):
            score2+=1 
            spawn_ball(RIGHT)
        else:
            ball_vel[0]=-ball_vel[0]

    if ball_pos[0]>=(WIDTH-PAD_WIDTH-BALL_RADIUS):    
        if (ball_pos[1]<=(paddle2_pos[1]-PAD_HEIGHT/2)) or (ball_pos[1]>=(paddle2_pos[1]+PAD_HEIGHT/2)):
            score1+=1
            spawn_ball(LEFT)
        else:
            ball_vel[0]=-ball_vel[0]
    
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
     
    #draw ball
    c.draw_circle(ball_pos,BALL_RADIUS,5,"red")
   
    #update paddle's vertical position, kepp paddle on the screen
    paddle1_pos[1]+=paddle1_vel
    paddle2_pos[1]+=paddle2_vel
    if paddle1_pos[1]<=PAD_HEIGHT/2:
        paddle1_pos[1]=PAD_HEIGHT/2;
    if paddle1_pos[1]>=HEIGHT-PAD_HEIGHT/2:
        paddle1_pos[1]=HEIGHT-PAD_HEIGHT/2
    if paddle2_pos[1]<=PAD_HEIGHT/2:
        paddle2_pos[1]=PAD_HEIGHT/2;
    if paddle2_pos[1]>=HEIGHT-PAD_HEIGHT/2:
        paddle2_pos[1]=HEIGHT-PAD_HEIGHT/2
    
    #draw paddles
    c.draw_line([0,paddle1_pos[1]-PAD_HEIGHT/2],[PAD_WIDTH,paddle1_pos[1]-PAD_HEIGHT/2],1,"white")
    c.draw_line([0,paddle1_pos[1]+PAD_HEIGHT/2],[PAD_WIDTH,paddle1_pos[1]+PAD_HEIGHT/2],1,"white")
    c.draw_line([WIDTH-PAD_WIDTH,paddle2_pos[1]-PAD_HEIGHT/2],[WIDTH,paddle2_pos[1]-PAD_HEIGHT/2],1,"white")
    c.draw_line([WIDTH-PAD_WIDTH,paddle2_pos[1]+PAD_HEIGHT/2],[WIDTH,paddle2_pos[1]+PAD_HEIGHT/2],1,"white")
    
    #draw scores
    c.draw_text(str(score1),[280,100],24,"white")
    c.draw_text(str(score2),[320,100],24,"white")

def keydown(key):
    global paddle1_vel,paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel=-vel
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel=vel
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel=-vel
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel=vel
    
def keyup(key):
    global paddle1_vel,paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel=0
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel=0
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel=0
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel=0

def tick():
    global ball_vel
    ball_vel[0]=float(ball_vel[0])*1.2
    ball_vel[1]=float(ball_vel[1])*1.2
    
#create frame
frame=simplegui.create_frame("Pong",WIDTH,HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer=simplegui.create_timer(3000,tick)
frame.add_button("Reset",new_game,100)

#start frame
new_game()
frame.start()	