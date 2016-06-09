import simplegui
val=0
massage="0:00.0"
massage2="0/0"
time=0
points=0

def start():
    timer.start()
    
def stop():
    global time,points
    timer.stop()
    time+=1
    if (val % 5)==0:
        points=points+1
        
def reset():
    global val
    val=0
    time=0
    points=0
    
def value():
    global val
    val+=1

def draw(canvas):
    global val,massage,massage2
    min=int(val/600)
    sec=val-min*600
    massage=str(min)+":"+str("%04.1f"%(float(sec)/10))
    massage2=str(time)+"/"+str(points)
    canvas.draw_text(massage,[100,100],36,"red")
    canvas.draw_text(massage2,[250,20],20,"yellow")

frame=simplegui.create_frame("timer",300,200)
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)
frame.set_draw_handler(draw)
timer=simplegui.create_timer(100,value)
frame.start()