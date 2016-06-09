import simplegui

store=12
operand=3

def output():
    global store,operand
    print "store =",store
    print "operand=",operand
    print ""

def swap():
    global store,operand
    store,operand=operand,store
    output()
    
def add():
    global store,operand
    store=store+operand
    output()

def sub():
    global store,operand
    store=store-operand
    output()

def mul():
    global store,operand
    store*=operand
    output()

def div():
    global store,operand
    store=store/operand
    output()
    
def enter(inp):
    global operand
    operand=int(inp)

frame=simplegui.create_frame("calculator",200,200)
frame.add_button("Print",output)
frame.add_button("Swap",swap)
frame.add_button("Add",add)
frame.add_button("Sub",sub)
frame.add_button("Mul",mul)
frame.add_button("Div",div)
inp=frame.add_input("Enter a number",enter,100)

frame.start()

