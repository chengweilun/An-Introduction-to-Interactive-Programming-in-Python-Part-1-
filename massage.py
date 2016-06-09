import simplegui
import random
massage="hello,python"
interval=2000
width=500
height=500
position=[50,50]

def update(text):
    global massage
    massage=text
    
def tick():
    x=random.randrange(1,width)
    y=random.randrange(1,height)
    position[0]=x
    position[1]=y
    
def draw(canvas):
    canvas.draw_text(massage,position,36,"red")

frame=simplegui.create_frame("home",width,height)
text=frame.add_input("Massage:",update,150)
frame.set_draw_handler(draw)
timer=simplegui.create_timer(interval,tick)

frame.start()
timer.start()