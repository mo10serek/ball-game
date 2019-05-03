import pygame
import random
import sys
import math
import time
import os

# import the pygame constants (specifically the key codes and event types)
from pygame.locals import *

#soundCheer = pygame.mixer.Sound('c.wav')

# constants for accessing the attributes of the mouse
MOUSE_LMB = 0
MOUSE_RMB = 1
MOUSE_X   = 2
MOUSE_Y   = 3

pygame.mixer.init(22050, -16, 2, 4096)  # Initialize the mixer module.
soundBounce = pygame.mixer.Sound('bounce.wav')  # Load a sound.
soundExplostion = pygame.mixer.Sound('Explosion.wav')

# the resolution of the display window (but please note that the toy runs in fullscreen mode)
window_wid = 1000
window_hgt = 800

# wall locations
row = 0

xPositions = [40 ,65 ,90 ,115,140,165,190,215,240,265,290,315,340,365,390,415,440,465,490,515,540,565,590,615,640,665,690,715,740,
              40,             140,                                                                            640,            740,
              40,             140,                                                                            640,            740,
              40,             140,            240,265,290,315,340,365,390,415,        490,515,540,565,        640,            740,
              40,             140,            240,                                    490,        565,        640,            740,
              40,             140,            240,                                    490,        565,        640,            740,
              40,             140,            240,        315,340,365,390,415,440,465,490,        565,        640,            740,
              40,             140,            240,                                                565,        640,            740,
              40,             140,            240,                                                565,        640,            740,
              40,             140,165,190,215,240,265,290,315,340,365,390,415,440,465,490,        565,        640,            740,
              40,                                     290,                            490,        565,        640,            740,
              40,                                     290,                            490,        565,        640,            740,
              40,         115,140,165,190,215,        290,                415,        490,        565,        640,            740,
              40,         115,            215,        290,                415,        490,        565,        640,            740,
              40,         115,            215,        290,                415,        490,        565,        640,            740,
              40,         115,            215,        290,                415,        490,515,540,565,        640,            740,
              40,                                                         415,                                640,            740,
              40,                                                         415,                                640,            740,
              40,         115,140,165,190,215,        290,        365,390,415,440,465,490,515,540,565,590,615,640,            740,
              40,         115,                        290,        365,    415,                                                740,
              40,         115,                        290,        365,    415,                                                740,
              40,         115,        190,215,        290,        365,390,415,        490,515,540,565,590,615,640,665,690,715,740,
              40,         115,            215,        290,                                                                    740,
              40,         115,            215,        290,                                                                    740,
              40,         115,140,165,190,215,        290,315,340,365,390,415,        490,515,540,565,590,615,640,            740,
              40,                                                         415,                                                740,
              40,                                                         415,                                                740,
              40,                                                         415,                                                740,
              40 ,65 ,90 ,115,140,165,190,215,240,265,290,315,340,365,390,415,440,465,490,515,540,565,590,615,640,665,690,715,740,]
              
              
      
              
yPositions = [50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,50 ,
              75 ,            75 ,                                                                            75 ,            75 ,
              100,            100,                                                                            100,            100,
              125,            125,            125,125,125,125,125,125,125,125,        125,125,125,125,        125,            125,
              150,            150,            150,                                    150,        150,        150,            150,
              175,            175,            175,                                    175,        175,        175,            175,
              200,            200,            200,        200,200,200,200,200,200,200,200,        200,        200,            200,
              225,            225,            225,                                                225,        225,            225,
              250,            250,            250,                                                250,        250,            250,
              275,            275,275,275,275,275,275,275,275,275,275,275,275,275,275,275,        275,        275,            275,       
              300,                                    300,                            300,        300,        300,            300,
              325,                                    325,                            325,        325,        325,            325,
              350,        350,350,350,350,350,        350,                350,        350,        350,        350,            350,
              375,        375,            375,        375,                375,        375,        375,        375,            375,
              400,        400,            400,        400,                400,        400,        400,        400,            400,
              425,        425,            425,        425,                425,        425,425,425,425,        425,            425,
              450,                                                        450,                                450,            450,
              475,                                                        475,                                475,            475,
              500,        500,500,500,500,500,        500,        500,500,500,500,500,500,500,500,500,500,500,500,            500,
              525,        525,                        525,        525,    525,                                                525,
              550,        550,                        550,        550,    550,                                                550,
              575,        575,        575,575,        575,        575,575,575,        575,575,575,575,575,575,575,575,575,575,575,
              600,        600,            600,        600,                                                                    600,
              625,        625,            625,        625,                                                                    625,
              650,        650,650,650,650,650,        650,650,650,650,650,650,        650,650,650,650,650,650,650,650,        650,
              675,                                                        675,                                                675, 
              700,                                                        700,                                                700,
              725,                                                        725,                                                725,
              750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750]

row = len(xPositions)  

print(row)     
              
# change background
changeBackground = 1
changeBlock = 1              
   
# the frame rate is the number of frames per second that will be displayed and although
# we could (and should) measure the amount of time elapsed, for the sake of simplicity
# we will make the (not unreasonable) assumption that this "delta time" is always 1/fps
frame_rate = 30
delta_time = 1 / frame_rate

# change scenes
scene = "main Menu"
   
# these are the colours through which the game objects can be "cycled"
included_colours = []
included_colours.append(Color(255, 0, 0))
included_colours.append(Color(0, 255, 0))
included_colours.append(Color(0, 0, 255))
included_colours.append(Color(255, 255, 0))

# these are the unique identifiers for the game objects
object_unique_id = 1000

# this is the only game object included in the "toy" - rename it when5 you decide what
# these objects will represent within the "magic circle" of your final game submission
# and feel free to modify it as required, as long as you preserve the core mechanics 
class Object:

    def __init__(self):

		# get the next unique identifier and increment
        global object_unique_id
        self.id = object_unique_id
        object_unique_id += 1
	
		# the radius of the game object is fixed
        self.radius = 10
		
		# the initial colour is randomly selected and the "focus" flag is false
        self.colour = random.randint(0, len(included_colours) - 1)
        self.flag = False
        self.isItBall = True
        self.stop = False
        
		# (x, y) / (dx, dy) / (ddx, ddy) is the position / velocity / acceleration
        self.originalX = 0
        self.originalY = 0
        self.x = self.originalX #random.randint(self.radius, window_wid - 1 - self.radius)
        self.y = self.originalY #random.randint(self.radius, window_hgt - 1 - self.radius)
        angle = random.randint(0, 359)
        
        self.dx = 0
        self.dy = 0	
        self.store_dx = math.cos(math.radians(angle)) * 0.5
        self.store_dy = math.sin(math.radians(angle)) * 0.5	
        self.ddx = 0
        self.ddy = 0



def get_all_inputs():

	# get the state of the mouse (i.e., button states and pointer position)
	mouse_dict = {}
	(mouse_dict[MOUSE_LMB], _, mouse_dict[MOUSE_RMB]) = pygame.mouse.get_pressed()
	(mouse_dict[MOUSE_X], mouse_dict[MOUSE_Y]) = pygame.mouse.get_pos()

	# get the state of the keyboard
	keybd_tupl = pygame.key.get_pressed()
		
	# look in the event queue for the quit event
	quit_ocrd = False
	for evnt in pygame.event.get():
		if evnt.type == QUIT:
			quit_ocrd = True

	# return all possible inputs
	return mouse_dict, keybd_tupl, quit_ocrd
	

def update_all_game_objects(game_objects, mouse_dict):

    bounceOffWall(game_objects[0])
    bounceOffWall(game_objects[1])
    bounceOffWall(game_objects[2])
    bounceOffWall(game_objects[3])

	# visit all the game objects...
    for object in game_objects:
        
        # reset the flags
        object.flag = False
        
        if (object.x < 0) or (object.x > window_wid):
            object.dx = -object.dx
                
        if (object.y < 0) or (object.y > window_hgt):
            object.dy = -object.dy
        
        mouseX,mouseY = pygame.mouse.get_pos()
                
		# if the game object is beneath the mouse...
        if ((object.x - mouse_dict[MOUSE_X]) ** 2 + (object.y - mouse_dict[MOUSE_Y]) ** 2) < (object.radius ** 2):
	
			# ...then set the flag on that one
            object.flag = True
			
			# if the left button is clicked, change the colour
            if (mouse_dict[MOUSE_LMB]) and (object.stop == False) and (object.isItBall):
			
                object.colour = (object.colour + 1) % len(included_colours)
				
			# if the right button is clicked, attract all other objects of the same colour
            elif mouse_dict[MOUSE_RMB]:
			
                for another in game_objects:
				
                    if another.id != object.id and another.colour == object.colour and another.isItBall and another.stop == False:
					
                        delta_x = object.x - another.x
                        delta_y = object.y - another.y
                        magnitude = math.sqrt(delta_x ** 2 + delta_y ** 2)
						
                        another.dx = another.dx + (delta_x / magnitude) / 2
                        another.dy = another.dy + (delta_y / magnitude) / 2
	
		# update the positions
        object.x += object.dx
        object.y += object.dy	
		
    return game_objects
    
def bounceOffWall(object):
    
    if (40 <= object.x - object.radius <= 765) and (50 <= object.y - object.radius <= 75): #Top
        soundBounce.play()
        object.dy *= -1
    
    if (40 <= object.x - object.radius <= 65) and (50 <= object.y - object.radius <= 775): #left
        soundBounce.play()
        object.dx *= -1
    
    if (40 <= object.x - object.radius <= 765) and (750 <= object.y - object.radius <= 775): #bottom
        soundBounce.play()
        object.dy *= -1
    
    if (740 <= object.x - object.radius <= 765) and (50 <= object.y - object.radius <= 775): #right
        soundBounce.play()
        object.dx *= -1
  
    
    if (140 <= object.x - object.radius <= 165) and (75 <= object.y - object.radius <= 300): #A
        soundBounce.play()
        object.dx *= -1
        
    if (140 <= object.x - object.radius <= 515) and (275 <= object.y - object.radius <= 300): #B
        soundBounce.play()
        object.dy *= -1
        
    if (240 <= object.x - object.radius <= 265) and (125 <= object.y - object.radius <= 300): #C
        soundBounce.play()
        object.dx *= -1
    
    if (240 <= object.x - object.radius <= 440) and (125 <= object.y - object.radius <= 150): #D
        soundBounce.play()
        object.dy *= -1
        
        
    if (490 <= object.x - object.radius <= 590) and (125 <= object.y - object.radius <= 150): #E
        soundBounce.play()
        object.dy *= -1
        
    
    if (640 <= object.x - object.radius <= 665) and (75 <= object.y - object.radius <= 500): #F
        soundBounce.play()
        object.dx *= -1
        
    if (490 <= object.x - object.radius <= 515) and (125 <= object.y - object.radius <= 225): #G  
        soundBounce.play()
        object.dx *= -1
        
    if (565 <= object.x - object.radius <= 590) and (125 <= object.y - object.radius <= 450): #H
        soundBounce.play()
        object.dx *= -1
    
    if (290 <= object.x - object.radius <= 515) and (200 <= object.y - object.radius <= 225): #I
        soundBounce.play()
        object.dy *= -1    
    
    if (115 <= object.x - object.radius <= 140) and (350 <= object.y - object.radius <= 450): #K
        soundBounce.play()
        object.dx *= -1
    
    if (115 <= object.x - object.radius <= 240) and (350 <= object.y - object.radius <= 375): #J
        soundBounce.play()
        object.dy *= -1  
    
    if (215 <= object.x - object.radius <= 240) and (350 <= object.y - object.radius <= 450): #L
        soundBounce.play()
        object.dx *= -1
    
    if (340 <= object.x - object.radius <= 365) and (300 <= object.y - object.radius <= 450): #M
        soundBounce.play()
        object.dx *= -1
     
    if (415 <= object.x - object.radius <= 440) and (350 <= object.y - object.radius <= 600): #N
        soundBounce.play()
        object.dx *= -1
        object.dy *= -1
        
    if (490 <= object.x - object.radius <= 515) and (300 <= object.y - object.radius <= 450): #O
        soundBounce.play()
        object.dx *= -1
        
    if (490 <= object.x - object.radius <= 590) and (450 <= object.y - object.radius <= 475): #P
        soundBounce.play()
        object.dy *= -1 
        
    if (115 <= object.x - object.radius <= 240) and (500 <= object.y - object.radius <= 525): #Q
        soundBounce.play()
        object.dy *= -1 
    
    if (365 <= object.x - object.radius <= 665) and (500 <= object.y - object.radius <= 525): #R
        soundBounce.play()
        object.dy *= -1 
        
    if (115 <= object.x - object.radius <= 140) and (500 <= object.y - object.radius <= 675): #S
        soundBounce.play()
        object.dx *= -1
     
    if (190 <= object.x - object.radius <= 240) and (575 <= object.y - object.radius <= 600): #T
        soundBounce.play()
        object.dx *= -1
        object.dy *= -1
    
    if (115 <= object.x - object.radius <= 240) and (650 <= object.y - object.radius <= 675): #U
        soundBounce.play()
        object.dy *= -1
       
    if (215 <= object.x - object.radius <= 240) and (575 <= object.y - object.radius <= 675): #V
        soundBounce.play()
        object.dx *= -1   
    
    if (290 <= object.x - object.radius <= 315) and (500 <= object.y - object.radius <= 675): #W
        soundBounce.play()
        object.dx *= -1  
        
    if (365 <= object.x - object.radius <= 390) and (500 <= object.y - object.radius <= 600): #X
        soundBounce.play()
        object.dx *= -1  
    
    if (290 <= object.x - object.radius <= 440) and (650 <= object.y - object.radius <= 675): #Y
        soundBounce.play()
        object.dy *= -1
        
    if (365 <= object.x - object.radius <= 440) and (575 <= object.y - object.radius <= 600): #Z
        soundBounce.play()
        object.dy *= -1
        
    if (490 <= object.x - object.radius <= 740) and (575 <= object.y - object.radius <= 600): #AA
        soundBounce.play()
        object.dy *= -1  
       
    if (490 <= object.x - object.radius <= 690) and (650 <= object.y - object.radius <= 675): #AB
        soundBounce.play()
        object.dy *= -1  
    
    if (415 <= object.x - object.radius <= 440) and (650 <= object.y - object.radius <= 750): #AC
        soundBounce.play()
        object.dx *= -1  
    
def main():
    
	# initialize pygame
    pygame.init()
	
    pygame.mixer.init(22050, -16, 2, 4096)  # Initialize the mixer module.
    soundBounce = pygame.mixer.Sound('bounce.wav')  # Load a sound.
    soundExplostion = pygame.mixer.Sound('Explosion.wav')
    #soundTorpito = pygame.mixer.Sound('rocket.mp3')
    
	# create the window and set the caption of the window
    window_sfc = pygame.display.set_mode( (window_wid, window_hgt) ) #, FULLSCREEN )
    pygame.display.set_caption('Balls in the labyrinth')
    
    # create all sprites
    # blocks
    block1 = pygame.transform.scale(pygame.image.load("Block.jpg").convert_alpha(), (100,100))
    block2 = pygame.transform.scale(pygame.image.load("Block2.png").convert_alpha(), (100,100))
    block3 = pygame.transform.scale(pygame.image.load("Block3.jpg").convert_alpha(), (100,100))
    block4 = pygame.transform.scale(pygame.image.load("Block4.jpg").convert_alpha(), (100,100))
    
    smallBlock1 = pygame.transform.scale(pygame.image.load("Block.jpg").convert_alpha(), (25,25))
    smallBlock2 = pygame.transform.scale(pygame.image.load("Block2.png").convert_alpha(), (25,25))
    smallBlock3 = pygame.transform.scale(pygame.image.load("Block3.jpg").convert_alpha(), (25,25))
    smallBlock4 = pygame.transform.scale(pygame.image.load("Block4.jpg").convert_alpha(), (25,25))
    
    #simple buttons
    play = pygame.transform.scale(pygame.image.load("play.png").convert_alpha(), (70, 70))
    customize = pygame.transform.scale(pygame.image.load("customize.png").convert_alpha(), (70, 70))
    
    left = pygame.transform.scale(pygame.image.load("left.png").convert_alpha(), (100,100))
    right = pygame.transform.rotate(left, 180)
    
    back = pygame.transform.scale(pygame.image.load("back.png").convert_alpha(), (100,100))
    left2 = pygame.transform.scale(pygame.image.load("left.png").convert_alpha(), (40,40))
    slow = pygame.transform.rotate(left2,90)
    
    #background
    backgroundMainMenu = pygame.transform.scale(pygame.image.load("mainMenu.jpg").convert_alpha(), (window_wid,window_hgt))
    
    backgroundOptions = pygame.transform.scale(pygame.image.load("customizeMenu.png").convert_alpha(), (window_wid,window_hgt))    
    
    background1 = pygame.transform.scale(pygame.image.load("background.jpg").convert_alpha(), (100,100))
    background2 = pygame.transform.scale(pygame.image.load("background2.png").convert_alpha(), (100,100))
    background3 = pygame.transform.scale(pygame.image.load("background3.jpg").convert_alpha(), (100,100))
    background4 = pygame.transform.scale(pygame.image.load("background4.jpg").convert_alpha(), (100,100))
    
    bigBackground1 = pygame.transform.scale(pygame.image.load("background.jpg").convert_alpha(), (window_wid,window_hgt))
    bigBackground2 = pygame.transform.scale(pygame.image.load("background2.png").convert_alpha(), (window_wid,window_hgt))
    bigBackground3 = pygame.transform.scale(pygame.image.load("background3.jpg").convert_alpha(), (window_wid,window_hgt))
    bigBackground4 = pygame.transform.scale(pygame.image.load("background4.jpg").convert_alpha(), (window_wid,window_hgt))

    background = pygame.transform.scale(pygame.image.load("background.jpg").convert_alpha(), (100,100))
    
    deepSea = pygame.transform.scale(pygame.image.load("deepSea.jpg").convert_alpha(),(window_wid,window_hgt))

    explostionBackground = pygame.transform.scale(pygame.image.load("explosion.jpg").convert_alpha(), (window_wid, window_hgt))
    
    # hazzarts
    bomb = pygame.transform.scale(pygame.image.load("bomb.jpg").convert_alpha(), (50,50))
    saw = pygame.transform.scale(pygame.image.load("SawBig.png").convert_alpha(), (50,50))
    
    # star
    star = pygame.transform.scale(pygame.image.load("star.jpg").convert_alpha(), (50, 50))
    
    #clip
    torpedo = pygame.transform.scale(pygame.image.load("torpedo.jpg").convert_alpha(), (30,240))
    rotatedTorpedo = pygame.transform.rotate(torpedo, 90)
    torpedo = rotatedTorpedo
    enemy = pygame.transform.scale(pygame.image.load("enemy.png").convert_alpha(), (int(window_wid/2), 500))
    explostion = pygame.transform.scale(pygame.image.load("explosion.jpg").convert_alpha(), (50, 50))
    
    # for changing the back ground and block
    block = block1
    background = background1
    
    leftButtonBlock = {"sprite": left,
                       "x": window_wid/2 - 250,
                       "y": window_hgt/2,
                       "xSize": 100,
                       "ySize": 100 }
    rightButtonBlock = {"sprite": right,
                       "x": window_wid/2 + 150,
                       "y": window_hgt/2,
                       "xSize": 100,
                       "ySize": 100 }   
    blockExample = {"sprite": block,
                    "x": window_wid/2 - 50,
                    "y": window_hgt/2,
                    "xSize": 100,
                    "ySize": 100 } 
    leftBackgroundBlock = {"sprite": left,
                           "x": window_wid/2 - 250,
                           "y": window_hgt/2 + 200,
                           "xSize": 100,
                           "ySize": 100 }   
    rightBackgroundBlock = {"sprite": right,
                           "x": window_wid/2 + 150,
                           "y": window_hgt/2 + 200,
                           "xSize": 100,
                           "ySize": 100 }  
    backgroundExample = {"sprite": background,
                         "x": window_wid/2 - 50,
                         "y": window_hgt/2 + 200,
                         "xSize": 100,
                         "ySize": 100 } 
    hazzarts = []
    
    hazzarts.append({"x": 165,
                     "y": 45,
                     "image": saw,
                     "type": "saw"
                     })                             
    hazzarts.append({"x": 530,
                     "y": 235,
                     "image": saw,
                     "type": "saw"})
    
    hazzarts.append({"x": 330,
                     "y": 295,
                     "image": saw,
                     "type": "saw"})
                     
    hazzarts.append({"x": 380,
                     "y": 460,
                     "image": bomb,
                     "type": "bomb"})
                     
    hazzarts.append({"x": 170,
                     "y": 400,
                     "image": bomb,
                     "type": "bomb"})
                     
    hazzarts.append({"x": 720,
                     "y": 520,
                     "image": saw,
                     "type": "saw"})
                     
    hazzarts.append({"x": 170,
                     "y": 650,
                     "image": saw,
                     "type": "saw"})
                     
    hazzarts.append({"x": 525,
                     "y": 370,
                     "image": star,
                     "type": "star",
                     "off": True})
                     
    hazzarts.append({"x": 525,
                     "y": 150,
                     "image": star,
                     "type": "star",
                     "off": True})
    
    hazzarts.append({"x": 165,
                     "y": 220,
                     "image": star,
                     "type": "star",
                     "off": True})
                     
    hazzarts.append({"x": 190,
                     "y": 600,
                     "image": star,
                     "type": "star",
                     "off": True})
    
    
    scene = "menu"
    
    # change background
    changeBackground = 1
    changeBlock = 1 
    
    playX = window_wid/2 - 175
    playY = 200
    customizeX = window_wid/2 + 50
    customizeY = 200
    customizeXYSize = 70
    
	# create a clock
    clock = pygame.time.Clock()
	
    for i in range(row):
        xPositions[i] += 15
        #yPositions[i] += 15
    
    number_of_objects = 4
    number_of_buttons = 4
    game_objects = []
    for i in range(number_of_objects):
        game_objects.append(Object())
        
    for j in range(number_of_buttons):
        game_objects.append(Object())        
        game_objects[i + j + 1].isItBall = False
    
    game_objects[0].x = 100
    game_objects[0].originalX = 100
    game_objects[0].y = 100
    game_objects[0].originalY = 100
            
    game_objects[1].x = 710
    game_objects[1].originalX = 710
    game_objects[1].y = window_hgt - 100
    game_objects[1].originalY = window_hgt - 100
            
    game_objects[2].x = window_wid/2 - 120
    game_objects[2].originalX = window_wid/2 - 120
    game_objects[2].y = window_hgt - 100
    game_objects[2].originalY = window_hgt - 100
            
    game_objects[3].x = 725
    game_objects[3].originalX = 725
    game_objects[3].y = 90
    game_objects[3].originalY = 90
    
    # top
    game_objects[4].x = window_wid/2
    game_objects[4].y = 20
    game_objects[4].radius = 20
    game_objects[4].colour = 0
                
    # left
    game_objects[5].x = 20
    game_objects[5].y = window_hgt/2
    game_objects[5].radius = 20
    game_objects[5].colour = 1
    
    # right
    game_objects[6].x = window_wid - 20
    game_objects[6].y = window_hgt/2
    game_objects[6].radius = 20
    game_objects[6].colour = 2
           
    # bottom
    game_objects[7].x = window_wid/2
    game_objects[7].y = window_hgt - 20
    game_objects[7].radius = 20
    game_objects[7].colour = 3
    
    torpedoVelocitiy = -10
    torpedoPosition = window_wid - window_wid/8
    haveNotExploded = True
    
    filled = 0
    counterRotate = 0

    # the game loop is a postcondition loop controlled using a Boolean flag
    closed_flag = False
    while not closed_flag:
        # get the inputs from the mouse and check if the window has been closed
        mouse_dict, keybd_tupl, closed_flag = get_all_inputs()
        if keybd_tupl[pygame.K_ESCAPE]:
            closed_flag = True
        if scene == "menu":
            #input
            if (playX <= mouse_dict[MOUSE_X] <= playX + 70) and (playY <= mouse_dict[MOUSE_Y] <= playY + 70) and (mouse_dict[MOUSE_LMB]):
                scene = "story"
                
                for object in game_objects:
                    pygame.draw.circle(window_sfc, included_colours[object.colour], (int(object.x), int(object.y)), object.radius)

            if (customizeX <= mouse_dict[MOUSE_X] <= customizeX + 70) and (customizeY <= mouse_dict[MOUSE_Y] <= customizeY + 70) and (mouse_dict[MOUSE_LMB]):
                scene = "customize"  
            
            #update
            haveNotExploded = True
            filled = 0
            
            #render
            # make the background
            window_sfc.blit(backgroundMainMenu,(0, 0))
        
            font = pygame.font.SysFont(None, 60)
            title = font.render("Balls in the labyrinth", True, (255,0,255))
            window_sfc.blit(title, (window_wid/4 +20 ,100))
    
            window_sfc.blit(play,(playX, playY))
            window_sfc.blit(customize,(customizeX, customizeY))
              
        
        if scene == "game":
            
            seconds = 9000
            counterRotate += 1
            
            #input
            if (window_wid - 100 <= mouse_dict[MOUSE_X] <= window_wid) and (20 <= mouse_dict[MOUSE_Y] < 120) and (mouse_dict[MOUSE_LMB]):
                scene = "menu"
            
            # update the positions and velocities of all the game objects in the toy
            game_objects = update_all_game_objects(game_objects, mouse_dict)
            
            # render the game objects to the display
            if (changeBackground == 1):
                window_sfc.blit(bigBackground1, (0,0))
            elif (changeBackground == 2):
                window_sfc.blit(bigBackground2, (0,0))
            elif (changeBackground == 3):
                window_sfc.blit(bigBackground3, (0,0))
            elif (changeBackground == 4):
                window_sfc.blit(bigBackground4, (0,0))
            
            for counter in range(0,row):
                if (changeBlock == 1):
                    window_sfc.blit(smallBlock1,(xPositions[counter],yPositions[counter]))
                elif (changeBlock == 2):
                    window_sfc.blit(smallBlock2,(xPositions[counter],yPositions[counter]))
                elif (changeBlock == 3):
                    window_sfc.blit(smallBlock3,(xPositions[counter],yPositions[counter]))
                elif (changeBlock == 4):
                    window_sfc.blit(smallBlock4,(xPositions[counter],yPositions[counter]))
            
            window_sfc.blit(back, (window_wid - 100,20))     
            
            for hazzart in hazzarts:
                if hazzart["type"] == "saw":
                    newHazzart = pygame.transform.rotate(hazzart["image"], counterRotate)
                    window_sfc.blit(newHazzart,(hazzart["x"],hazzart["y"]))
                else:
                    window_sfc.blit(hazzart["image"],(hazzart["x"],hazzart["y"]))
                
                for object in game_objects:
                    if (hazzart["x"] <= object.x) and (object.x <= hazzart["x"] + 50) and (hazzart["y"] <= object.y) and (object.y <= hazzart["y"] + 50):
                        if hazzart["type"] == "saw":
                            object.x = object.originalX
                            object.y = object.originalY
                            object.dx = 0
                            object.dy = 0
                        if hazzart["type"] == "bomb":
                            scene = "game Over"
                        if hazzart["type"] == "star":
                            object.stop = True
                            object.x = hazzart["x"] + 25
                            object.y = hazzart["y"] + 25
                            object.dx = 0
                            object.dy = 0
                            if (hazzart["off"]):
                                filled += 1
                                hazzart["off"] = False
                            print(filled)     
            
            if filled == 4:
                scene = "finish"
            
            # draw each of the game objects and encircle the one that is flagged
            for object in game_objects:
                if (window_wid/2 + 100 < mouse_dict[MOUSE_X]) and (mouse_dict[MOUSE_X] < window_wid/2 + 140) and (window_hgt - 40 < mouse_dict[MOUSE_Y]) and (mouse_dict[MOUSE_Y] <window_hgt) and mouse_dict[MOUSE_LMB] and object.isItBall and not object.x == 0 and not object.y == 0:
                    object.dx -= 1
                    object.dy -= 1
                pygame.draw.circle(window_sfc, included_colours[object.colour], (int(object.x), int(object.y)), object.radius)
		
        if scene == "customize":
            #input
            if (leftButtonBlock['x'] <= mouse_dict[MOUSE_X] <= leftButtonBlock["x"] + leftButtonBlock["xSize"]) and (leftButtonBlock["y"] <= mouse_dict[MOUSE_Y] <= leftButtonBlock["y"] + leftButtonBlock["ySize"]) and (mouse_dict[MOUSE_LMB]):
                pygame.time.wait(100)
                changeBlock -= 0.5
            elif (rightButtonBlock["x"] <= mouse_dict[MOUSE_X] <= rightButtonBlock["x"] + rightButtonBlock["xSize"]) and (rightButtonBlock["y"] <= mouse_dict[MOUSE_Y] <= rightButtonBlock["y"] + rightButtonBlock["ySize"]) and (mouse_dict[MOUSE_LMB]):
                pygame.time.wait(100)
                changeBlock += 0.5 
            elif (leftBackgroundBlock["x"] <= mouse_dict[MOUSE_X] <= leftBackgroundBlock["x"] + leftBackgroundBlock["xSize"]) and (leftBackgroundBlock["y"] <= mouse_dict[MOUSE_Y] <= leftBackgroundBlock["y"] + leftBackgroundBlock["ySize"]) and (mouse_dict[MOUSE_LMB]):
                pygame.time.wait(100)
                changeBackground -= 0.5
            elif (rightBackgroundBlock["x"] <= mouse_dict[MOUSE_X] <= rightBackgroundBlock["x"] + rightBackgroundBlock["xSize"]) and (rightBackgroundBlock["y"] <= mouse_dict[MOUSE_Y] <= rightBackgroundBlock["y"] + rightBackgroundBlock["ySize"]) and (mouse_dict[MOUSE_LMB]):
                pygame.time.wait(100)
                changeBackground += 0.5
            elif (20 <= mouse_dict[MOUSE_X] <= 120) and (20 <= mouse_dict[MOUSE_Y] < 120) and (mouse_dict[MOUSE_LMB]):
                scene = "menu"
            
            #update
            
            font = pygame.font.SysFont(None, 60)
            
            title = font.render("Options", True, (255,255,0))
            backgroundWords = font.render("Background", True, (255,255,0))
            blockWords = font.render("Block", True, (255,255,0))
            
            
            if changeBlock == 0:
                changeBlock = 4
            elif changeBlock == 5:
                changeBlock = 1
            
            if changeBackground == 0:
                changeBackground = 4
            elif changeBackground == 5:
                changeBackground = 1
                
            if changeBlock == 1:
                blockExample["sprite"] = block1
                block = block1
            elif changeBlock == 2:
                blockExample["sprite"] = block2
                block = block2
            elif changeBlock == 3:
                blockExample["sprite"] = block3
                block = block3
            elif changeBlock == 4:
                blockExample["sprite"] = block4
                block = block4
            
            if changeBackground == 1:
                backgroundExample["sprite"] = background1
                background = background1
            elif changeBackground == 2:
                backgroundExample["sprite"] = background2
                background = background2
            elif changeBackground == 3:
                backgroundExample["sprite"] = background3
                background = background3
            elif changeBackground == 4:
                backgroundExample["sprite"] = background4
                background = background4
                
            #render
            window_sfc.blit(backgroundOptions, (0,0))
            window_sfc.blit(leftButtonBlock['sprite'], (leftButtonBlock['x'] ,leftButtonBlock['y']))
            window_sfc.blit(rightButtonBlock['sprite'], (rightButtonBlock['x'] ,rightButtonBlock['y']))
            window_sfc.blit(leftBackgroundBlock['sprite'], (leftBackgroundBlock['x'],leftBackgroundBlock['y']))
            window_sfc.blit(rightBackgroundBlock['sprite'], (rightBackgroundBlock['x'] ,rightBackgroundBlock["y"]))
            window_sfc.blit(block, (window_wid/2 - 50, window_hgt/2))
            window_sfc.blit(background, (window_wid/2 - 50, window_hgt/2 +200))
            window_sfc.blit(back, (20,20))
            window_sfc.blit(title, (window_wid/2-80, window_hgt/4))
            window_sfc.blit(blockWords, (window_wid/2 - 130,  window_hgt/2 - 50))
            window_sfc.blit(backgroundWords, (window_wid/2 - 70,window_hgt/2 + 150))
            
            
        if scene == "story":
            #input
            if (mouse_dict[MOUSE_LMB]) and (750 < mouse_dict[MOUSE_Y]):
                scene = "game"
            
            #font
            font = pygame.font.SysFont(None, 30)
            
            description1 = font.render("You are the captain of a submarine that crushed with the enemy ship.", True, (255,255,0))
            description2 = font.render("Water is slowly flooding your ship. into star-shaped holes.", True, (255,255,0))
            description3 = font.render("You need to close four main valves in your ship so water does not flood your ", True, (255,255,0))
            description4 = font.render("submarine and you can save your crew.", True, (255,255,0))
            description5 = font.render("To block four main channels and close four valves you need to drop four coloured balls",True, (255,255,0))
            description6 = font.render("In this game, your goal is to tilt a two-dimensional maze so that the ball can move to the hole.",True, (255,255,0))
            description7 = font.render("The labyrinth is dangerous and filled with traps and explosives.",True, (255,255,0))
            gameInstructions1 = font.render("To change the color of the ball, you need to press one the balls with your left button on the mouse" , True, (255,0,0))
            gameInstructions2 = font.render("press the one of the buttons with the right button on the mouse" , True, (255,0,0))
            gameInstructions3 = font.render("that are on the top, left, right, bottom so it" , True, (255,0,0))
            gameInstructions4 = font.render("move the balls towards the buttons that have the same color to the button", True, (255,0,0))
            gameInstructions5 = font.render("you make the balls to avoid these hazards", True, (0,255,0))
            gameInstructions6 = font.render("Saws: when the balls touch them, it brings it back to its original location", True, (0,255,0))
            gameInstructions7 = font.render("Bombs: when the balls touch them, it is GAME OVER", True, (0,255,0))
            gameInstructions8 = font.render("To finish the game, you need to put each ball to a different star", True, (0,255,255))
            gameInstructions9 = font.render("and you are able to save your ship and defeat the enemy ship", True, (0,255,255))
            gameInstructions10 = font.render("Good Luck", True, (255,0,255))
            enter = font.render("Click here to continue", True, (255,255,0))
            
            #update
            for object in game_objects:
                if object.isItBall:
                    object.x = object.originalX
                    object.y = object.originalY
                    object.dx = 0
                    object.dy = 0
            filled = 0  
            counterRotate = 0
            
            #render
            window_sfc.blit(backgroundOptions, (0,0))
            
            window_sfc.blit(description1, (15,15))
            window_sfc.blit(description2, (15,40))
            window_sfc.blit(description3, (15,65))
            window_sfc.blit(description4, (15,90))
            window_sfc.blit(description5, (15,115))
            window_sfc.blit(description6, (15,150))
            window_sfc.blit(description7, (15,185))
            
            window_sfc.blit(gameInstructions1, (20, 230))
            window_sfc.blit(gameInstructions2, (20, 255))
            window_sfc.blit(gameInstructions3, (20, 280))
            window_sfc.blit(gameInstructions4, (20, 305))
            
            pygame.draw.circle(window_sfc, (255,0,0), (int(window_wid/4 - 100), 370), 30)
            pygame.draw.circle(window_sfc, (0,255,0), (int(window_wid/4 + 100), 370), 30)
            pygame.draw.circle(window_sfc, (0,0,255), (int(3*window_wid/4 - 100), 370), 30)
            pygame.draw.circle(window_sfc, (255,255,0), (int(3*window_wid/4 + 100), 370), 30)
            
            window_sfc.blit(saw, (30, 410))
            window_sfc.blit(bomb, (70, 410))
            window_sfc.blit(gameInstructions5, (110, 410))
            window_sfc.blit(gameInstructions6, (110, 435))
            window_sfc.blit(gameInstructions7, (110, 460))
            
            window_sfc.blit(star, (window_wid - 200,500))
            window_sfc.blit(gameInstructions8, (window_wid/4 - 100, 510))
            window_sfc.blit(gameInstructions9, (window_wid/4 - 100, 535))
            
            window_sfc.blit(gameInstructions10, (window_wid/2 - 20, 600))
            
            window_sfc.blit(enter, (window_wid - window_wid/4 - 100, window_hgt - 40))
           
            for object in game_objects:
                if object.isItBall:
                    object.colour = random.randint(0, len(included_colours) - 1)
            
        if scene == "finish":
            pygame.mixer.music.load('rocket.mp3')
            pygame.mixer.music.play(-1)
            window_sfc.blit(deepSea, (0,0))
            
            #font
            fontBig = pygame.font.SysFont(None, 80)
            fontSmall = pygame.font.SysFont(None, 30)
            
            #animation
            window_sfc.blit(torpedo, (torpedoPosition, window_hgt/2 ))
            window_sfc.blit(enemy, (int(window_wid/8 + 200 - window_wid/4), window_hgt/2 - 250))
            torpedoPosition += torpedoVelocitiy
            wining1 = fontBig.render("You Win", True, (0,255,255))
            wining2 = fontSmall.render("You are able to save your submarine and destroy the enemy ship.", True, (0,0,255))
            wining3 = fontSmall.render("All the crew cheers for you for saving them.", True, (0,0,255))
            wining4 = fontSmall.render("Now you can able to rise your submarine to the surface and celebrate your victory.", True, (0,0,255))
            wining5 = fontBig.render("\"Glory to our Captain\"", True, (0,0,255))
            
            if torpedoPosition - 50 < window_wid/2:
                #input

                pygame.mixer.music.stop()
                window_sfc.blit(deepSea, (0,0))
                window_sfc.blit(explostionBackground, (0,0))
                window_sfc.blit(back, (window_wid/2-50,510))
                #soundCheer.play()
                if (haveNotExploded):
                    soundExplostion.play()
                    haveNotExploded = False
                window_sfc.blit(wining1, (window_wid/2 - 180,200))
                window_sfc.blit(wining2, (window_wid/2 - 330, 300))
                window_sfc.blit(wining2, (window_wid/2 - 330, 350))
                window_sfc.blit(wining4, (window_wid/2 - 390, 400))
                window_sfc.blit(wining5, (window_wid/2 - 270, 450))
                
                if (window_wid/2-50 <= mouse_dict[MOUSE_X] <= window_wid/2 + 50) and (460 <= mouse_dict[MOUSE_Y] < 560) and (mouse_dict[MOUSE_LMB]):
                    scene = "menu"
                
                
                 
        if scene == "game Over":
            #update
            window_sfc.blit(deepSea, (0,0))
            window_sfc.blit(explostionBackground, (0,0))
             
            if (haveNotExploded):
                    soundExplostion.play()
                    haveNotExploded = False
            
            font = pygame.font.SysFont(None,80)
            
            #render
            window_sfc.blit(deepSea, (0,0))
            window_sfc.blit(explostionBackground, (0,0))
             
            if (haveNotExploded):
                    soundExplostion.play()
                    haveNotExploded = False
            gameOver = font.render("GAME OVER", True, (0,255,255))
            description1 = font.render("You lost your ship", True, (0,255,255))
            
            window_sfc.blit(gameOver, (window_wid/2-200, 200))
            window_sfc.blit(description1, (window_wid/2-270, 300))
            window_sfc.blit(back, (window_wid/2 - 50,400))
             
            if (mouse_dict[MOUSE_LMB]) and (window_wid/2 - 50 < mouse_dict[MOUSE_X]) and (mouse_dict[MOUSE_X] < window_wid/2 + 50) and (400 < mouse_dict[MOUSE_Y]) and (mouse_dict[MOUSE_Y] < 500):
                scene = "menu"
        
        # update the display and enforce the minimum frame rate
        pygame.display.update()
        clock.tick(frame_rate)

		
if __name__ == "__main__":
	main()