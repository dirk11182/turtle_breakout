import turtle
import numpy as np
import time

class Sprite(object):
    def __init__(self, pos=(0,0), shape=(1,1), color="red"):
        self.pos = np.array(pos)
        self.w = 20
        self.h = 20
        self.rect = {"pos":self.pos, "w":self.w*shape[0], "h":self.h*shape[1]}
        self.shape = shape
        
        self.image = turtle.Turtle()
        self.image.speed(0)
        self.image.shape("square")
        self.image.color(color)
        #self.image.turtlesize(1,1,0)
        self.image.shapesize(stretch_wid=shape[1], stretch_len=shape[0])
        self.image.penup()
        self.image.goto(self.pos)
    
    def update(self, dt):
        pass
    
    def draw(self):
        pass

class HPadlle(Sprite):
    def __init__(self):        
        super().__init__(pos=(0, -200), shape=(6,0.5), color="white")
        # speed in x-direction speed <0: left; speed>0:right
        self.speed = 0
        
    def move(self, dx):
        self.pos[0] += dx        
        if(self.pos[0]<(-400+self.shape[0]*10)):
            self.pos[0] = -400+self.shape[0]*10
        if(self.pos[0]>(400-self.shape[0]*10)):
            self.pos[0] = 400-self.shape[0]*10
        self.rect["pos"] = self.pos
        self.image.goto(self.pos)
    
    def move_left(self):
        self.move(-20)

    def move_right(self):
        self.move(20)
    
    def set_speed(self, s):
        self.speed = s
    
    def get_speed(self):
        return(self.speed)
    
    def update(self, dt):
        pass

class Brick(Sprite):
    pass

## variable definition ##########################################
running = True
game_pause = True

paddle_a_y = 0
paddle_b_y = 0

## graphical object initiation/definition #######################
wn = turtle.Screen()
wn.title("Python-Spiele mit turtle")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# sprites
s1 = Sprite(pos=(-200,-30), shape=(3,5))
paddle = HPadlle()

## function definitions ########################################

def my_close():
    global running
    running=False

# key-binding ##################################################
wn.listen()
wn.onkeypress(my_close, "q")
wn.onkeypress(paddle.move_left, "Left")
wn.onkeypress(paddle.move_right, "Right")

t0 = time.time()
dt = 0
# game loop ####################################################
while(running):
    # timing
    time.sleep(0.05)
    dt = (t0-time.time())*1000
    
    # update
    paddle.update(dt)
    s1.update(dt)

    wn.update()
    
    # time management
    t0 = time.time()    
  
turtle.bye()
    
    