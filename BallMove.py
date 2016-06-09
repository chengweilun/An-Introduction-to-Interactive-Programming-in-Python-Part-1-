import simplegui
width=600
height=300
val=10
ball_pos=[width/2,height/2]

def keydown(key):
    global ball_pos
    if key ==simplegui.KEY_MAP["left"]:
        ball_pos[0]-=val;
    elif key ==simplegui.KEY_MAP["right"]:
        ball_pos[0]+=val
    elif key ==simplegui.KEY_MAP["up"]:
        ball_pos[1]-=val
    else:
        key==simplegui.KEY_MAP["down"]
        ball_pos[1]+=val

def draw(canvas):
    canvas.draw_circle(ball_pos,10,2,"red","white")
    
frame=simplegui.create_frame("ballmove",width,height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.start()