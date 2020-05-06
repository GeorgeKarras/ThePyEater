import pygame
import time                                       
import sys
from random import randint
import os

#reload(sys)
#print sys.path
#sys.path.append(".\\Sounds")
#sys.path.append(".\\Images")
#reload(sys)

#sys.setdefaultencoding("utf-8")

class Entity(pygame.sprite.Sprite):                 #sprite class
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    

class Head(Entity):                                 #class Head of snake
    speed=64
    xvel=speed
    yvel=0
    prev_x=0
    prev_y=0
    image=None
    direction="right"
    color=""
    next_move=""
    begin=False
    died=False
    create=True
    identity="Head"
    
    def __init__(self,x,y,color):                   #Head creation
        Entity.__init__(self)
        self.color=color
        if color=="yellow":
            self.image=yellow_right
        else:
            self.image=blue_right
        self.rect=pygame.Rect(x,y,self.image.get_rect().size[0],self.image.get_rect().size[1])
        self.mouth_rect=pygame.Rect(x+60,y+5,2,55)
            
    def update(self,right,left,down,up):        #update position, check collision

        if not self.begin:
            self.begin=True
        else:
            self.collide()
        
        self.prev_x=self.rect[0]
        self.prev_y=self.rect[1]
        self.rect.left+=self.xvel
        self.rect.top+=self.yvel

        if self.rect[0]<0 or self.rect[0]>width-64 or self.rect[1]>height-64 or self.rect[1]<0:
            
            action_channel.play(hit)
            self.died=True
            
        
        
        
        
        mouth.rect=pygame.Rect(self.rect[0]+5,self.rect[1]+3,56,58)
        
            
        if left:
            if self.next_move=="":
                if self.direction!="right":
                    self.next_move="left"
        if right:
            if self.next_move=="":
                if self.direction!="left":
                    self.next_move="right"
        if down:
            if self.next_move=="":
                if self.direction!="up":
                    self.next_move="down"
        if up:
            if self.next_move=="":
                if self.direction!="down":
                    self.next_move="up"
        
        if self.next_move=="right":
                if self.direction!="left":
                    self.xvel=self.speed
                    self.yvel=0
                    self.image=sprite[self.color][1]
        elif self.next_move=="left":
                if self.direction!="right":
                    self.xvel=-self.speed
                    self.yvel=0
                    self.image=sprite[self.color][2]
        elif self.next_move=="up":
                if self.direction!="down":
                    self.xvel=0
                    self.yvel=-self.speed
                    if self.direction=="right":
                        self.image=sprite[self.color][3]
                    elif self.direction=="left":
                        self.image=sprite[self.color][4]
        elif self.next_move=="down":
                if self.direction!="up":
                    self.xvel=0
                    self.yvel=self.speed
                    if self.direction=="right":
                        self.image=sprite[self.color][5]
                    elif self.direction=="left":
                        self.image=sprite[self.color][6]
                        
        if self.next_move!="":
                self.direction=self.next_move
        self.next_move=""
        
    def collide(self):
        for e in edibles:
            if pygame.sprite.collide_rect(mouth, e):
                if e.identity=="Body":
                    action_channel.play(hit)
                    self.died=True
                    return
                elif e.identity=="Apple":
                    if not self.died:
                        action_channel.play(eat)
                    edibles.remove(e)
                    del e
                    self.create=True        #create a new body and apple

class Mouth(Entity):
    owner=None
    
    def __init__(self,owner):
        Entity.__init__(self)
        self.rect=pygame.Rect(owner.rect[0]+10,owner.rect[1]+5,30,55)
        self.owner=owner
    
       
class Body(Entity):         #class for snake body
    speed=64
    image=None
    prev_x=0
    prev_y=0
    identity="Body"
    
    def __init__(self,previous):
        Entity.__init__(self)
        self.image=sprite[player[0].color][0]
        self.rect=pygame.Rect(previous.rect[0],previous.rect[1],self.image.get_rect().size[0],self.image.get_rect().size[1])
        
    def update(self,previous):

     self.prev_x=self.rect[0]
     self.prev_y=self.rect[1]
     self.rect[0]=previous.prev_x
     self.rect[1]=previous.prev_y
            
class Apple(Entity):        #class for apples
    identity="Apple"
    image=None

    def __init__(self,x,y,image):
        Entity.__init__(self)
        self.image=image
        self.rect=pygame.Rect(x,y,self.image.get_rect().size[0],self.image.get_rect().size[1])
        
    
def stop():             #function for pause
    sunexeia=False
    while not sunexeia:
        for e in pygame.event.get():
            if e.type==pygame.KEYDOWN and e.key==pygame.K_p:
                sunexeia=True


pygame.init()
pygame.mixer.init()

eat=pygame.mixer.Sound("eat.ogg")
menu=pygame.mixer.Sound("Menu_Music.ogg")
track=pygame.mixer.Sound("track.ogg")
hit=pygame.mixer.Sound("Fallen.ogg")


music_channel=pygame.mixer.Channel(0)
action_channel=pygame.mixer.Channel(1)


edibles=pygame.sprite.Group()

a=pygame.display.Info()


width=int(round((a.current_w/64),1)*64)
height=int(round((a.current_h/64),1)*64)

score=-10

myfont = pygame.font.SysFont("monospace", 15)
title=pygame.image.load("title.jpg")                               
title=pygame.transform.scale(title,[662,152]) 
logo=pygame.image.load("logo.jpg")                                 
logo=pygame.transform.scale(logo,[600,547])                        
enter=pygame.image.load("Enter.jpg")                               
enter=pygame.transform.scale(enter,[158,39]) 
choose=pygame.image.load("choose.jpg")                             
choose=pygame.transform.scale(choose,[478,67])
snake=pygame.image.load("blue_snake.jpg")                          
snake=pygame.transform.scale(snake,[367,609])
snake1=pygame.image.load("yellow_snake.jpg")                       
snake1=pygame.transform.scale(snake1,[373,617])
options=pygame.image.load("game_options.png")                      
options=pygame.transform.scale(options,[287,57])
controls=pygame.image.load("controls.png")                         
controls=pygame.transform.scale(controls,[171,64])
up_im=pygame.image.load("up.png")
up_im=pygame.transform.scale(up_im,[71,76])
left_im=pygame.image.load("left.png")
left_im=pygame.transform.scale(left_im,[71,76])
right_im=pygame.image.load("right.png")
right_im=pygame.transform.scale(right_im,[71,76])
down_im=pygame.image.load("down.png")
down_im=pygame.transform.scale(down_im,[71,76])
respawn=pygame.image.load("RESPAWN.png")                           
respawn=pygame.transform.scale(respawn,[250,71])
pause=pygame.image.load("PAUSE.png")                               
pause=pygame.transform.scale(pause,[190,63])
sound=pygame.image.load("sound.png")                               
sound=pygame.transform.scale(sound,[171,64])
info=pygame.image.load("Game_Info.png") 
info=pygame.transform.scale(info,[195,47])
gameplay=pygame.image.load("gameplay.png") 
gameplay=pygame.transform.scale(gameplay,[786,275])
enter2=pygame.image.load("enter2.png") 
enter2=pygame.transform.scale(enter2,[359,90])

final_exit=-1
position=[470,310]
black=(0,0,0)
grey=(128,128,128)
volume_button=pygame.image.load("koumpi_volume.png")
volume_button=pygame.transform.scale(volume_button,(10,20))

label2 = myfont.render(str(0), 1, (255,255,255))
volume=1.0

screen=pygame.display.set_mode((width,height))
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

yellow_body=pygame.image.load("yellow_body.jpg")
blue_body=pygame.image.load("blue_body.jpg")

yellow_right=pygame.image.load("yellow_head_right.jpg")
blue_right=pygame.image.load("blue_head_right.jpg")

yellow_left=pygame.image.load("yellow_head_left.jpg")
blue_left=pygame.image.load("blue_head_left.jpg")

yellow_up_right=pygame.image.load("yellow_head_up_going_right.jpg")
blue_up_right=pygame.image.load("blue_head_up_going_right.jpg")

yellow_up_left=pygame.image.load("yellow_head_up_going_left.jpg")
blue_up_left=pygame.image.load("blue_head_up_going_left.jpg")

yellow_down_right=pygame.image.load("yellow_head_down_going_right.jpg")
blue_down_right=pygame.image.load("blue_head_down_going_right.jpg")

yellow_down_left=pygame.image.load("yellow_head_down_going_left.jpg")
blue_down_left=pygame.image.load("blue_head_down_going_left.jpg")

sprite={}

sprite["yellow"]=[yellow_body,yellow_right,yellow_left,yellow_up_right,yellow_up_left,yellow_down_right,yellow_down_left]
sprite["blue"]=[blue_body,blue_right,blue_left,blue_up_right,blue_up_left,blue_down_right,blue_down_left]
    
selection=False
apple=pygame.image.load("apple.png")
left=right=up=down=False
player=[]
end=False

random_x=0
random_y=0

clock=pygame.time.Clock()

music_channel.play(menu)

progress=True                                                      
while progress:
    if not music_channel.get_busy():
        music_channel.play(menu)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:                                
            progress=False
            end=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                progress=False
            elif event.key==pygame.K_ESCAPE:
                progress=False
                end=True
    screen.fill([0,0,0])                                           
    screen.blit(title,[a.current_w/3.5,a.current_h/21])            
    screen.blit(logo,[a.current_w/3.5,a.current_h/4.5])            
    screen.blit(enter,[700,750])                                   
    
    pygame.display.flip()
    clock.tick(60)

if end:
    pygame.quit()

progress=True                                                      
while progress:
    if not music_channel.get_busy():
        music_channel.play(menu)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
           progress=False
           end=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                progress=False
            elif event.key==pygame.K_ESCAPE:
                progress=False
                end=True
                
    if pygame.mouse.get_pressed()[0]:
         x=pygame.mouse.get_pos()[0]
         y=pygame.mouse.get_pos()[1]
         if y<position[1]+20 and y>position[1]-10:
             if x>position[0]+5:
               if position[0]<=460:
                position[0]+=10
                volume+=0.1
                pygame.mixer.music.set_volume(volume)
                label2 = myfont.render(str(volume), 1, (255,255,255))                
                
             elif x<position[0]-5:
               if position[0]>=380:
                position[0]-=10
                volume-=0.1
                pygame.mixer.music.set_volume(volume)
                label2 = myfont.render(str(volume), 1, (255,255,255))
                
    music_channel.set_volume(volume)
    screen.fill([0,0,0])
    screen.blit(options,[650,50])
    screen.blit(controls,[80,200])
    screen.blit(up_im,[130,250])
    screen.blit(left_im,[58,313]) 
    screen.blit(right_im,[200,315])
    screen.blit(down_im,[128,380])
    screen.blit(respawn,[60,500])
    screen.blit(pause,[60,600])
    screen.blit(sound,[350,200])
    screen.blit(info,[650,200])
    screen.blit(gameplay,[650,275])    
    screen.blit(enter2,[650,600])    
    pygame.draw.line(screen,grey,(370,318),(470,318),4)
    screen.blit(volume_button,position)
    pygame.display.flip()
    clock.tick(60)


if end:
    pygame.quit()


progress=True                                                      
choice=0
final_choice=-1
color=[0,255,0]
while progress:
    if not music_channel.get_busy():
        music_channel.play(menu)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:                               
            progress=False
            end=True
        elif event.key==pygame.K_ESCAPE:
                progress=False
                end=True
        if final_choice==-1:
         if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                if choice==1:
                    choice=0
            elif event.key==pygame.K_RIGHT:
                if choice==0:
                    choice=1
            elif event.key==pygame.K_RETURN:
                final_choice=choice
                color=[255,0,0]
                progress=False
    screen.fill([0,0,0]) 
    screen.blit(choose,[520,100])
    if choice==0:
        pygame.draw.rect(screen,color,[50,50,460,680],4)
    else:
        pygame.draw.rect(screen,color,[1000,50,460,680],4)
    screen.blit(snake,[100,100])                              
    screen.blit(snake1,[1050,100])                            
    pygame.display.flip()
    clock.tick(60)

if end:
    pygame.quit()
exodos=False

while not exodos:
    action_channel.stop()
    score=-10
    final_exit=-1
    progress=True
    
    if choice==1:
        player.append(Head(0,0,"yellow"))
    else:
        player.append(Head(128,128,"blue"))
    edibles.add(player[0])
    player.append(Body(player[len(player)-1]))
    edibles.add(player[1])
    mouth=Mouth(player[0])
    music_channel.play(track)

    
    up=down=left=right=False
    
    while progress:
        if not music_channel.get_busy():
            music_channel.play(track)
  
        score_label = myfont.render("Score : "+str(score), 1, (0,255,0)) 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:                                
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    progress=False
                    exodos=True
                if event.key==pygame.K_p:
                    stop()
                if event.key==pygame.K_LEFT:
                    left=True
                if event.key==pygame.K_RIGHT:
                    right=True
                if event.key==pygame.K_DOWN:
                    down=True
                if event.key==pygame.K_UP:
                    up=True
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    left=False
                if event.key==pygame.K_RIGHT:
                    right=False
                if event.key==pygame.K_DOWN:
                    down=False
                if event.key==pygame.K_UP:
                    up=False
        
        screen.fill([0,0,0])

    
    
        fontana = pygame.font.SysFont('Comic Sans MS', 25)
    
    
        for i in range(0,len(player)):
            if i==0:
                player[i].update(right,left,down,up)
                if player[i].died:
                    break
                else:
                    if player[i].create:
                        score+=10
                        t=Body(player[len(player)-1])
                        player.append(t)
                        edibles.add(t)
                        while not selection:
                            selection=True
                            random_x=(randint(0,(width/64)-1)*64)+9
                            random_y=(randint(0,(height/64)-1)*64)+9
                            apple1=Apple(random_x,random_y,apple)
                            for e in edibles:
                                if e.rect.collidepoint(random_x,random_y):
                                    selection=False
                                    break
                        edibles.add(apple1)
                        screen.blit(apple1.image,(apple1.rect[0],apple1.rect[1]))
                        selection=False
                        player[i].create=False
                    else:
                        screen.blit(apple1.image,(apple1.rect[0],apple1.rect[1]))
                screen.blit(player[i].image,(player[i].rect[0],player[i].rect[1]))
            else:
                player[i].update(player[i-1])
                screen.blit(player[i].image,(player[i].rect[0],player[i].rect[1]))
        if player[0].died:
            break
        
        
        screen.blit(score_label,(5,5))
        pygame.display.flip()
        clock.tick(7) 
    music_channel.stop()
    for i in edibles:
        i.kill()
        edibles.remove(i)
    player=[]
   
    if not exodos:
        while 1:
            
            for e in pygame.event.get():
                if e.type==pygame.KEYDOWN:
                    if e.key==pygame.K_r:
                        final_exit=0
                        break
                    elif e.key==pygame.K_ESCAPE:
                        final_exit=1
                        break
            if final_exit!=-1:
                break
            message=fontana.render("Score : "+str(score),1,(0,255,0))
            screen.blit(message,((width/2)-100,320))
            message=fontana.render("Press Escape to exit",1,(255,0,0))
            screen.blit(message,((width/2)-180,380))
            message=fontana.render("Press R to play again",1,(255,0,0))
            screen.blit(message,((width/2)-180,410))
            pygame.display.flip()
            clock.tick(60)
        if final_exit==1:
            exodos=True

#sys.path.append(os.getcwd())

pygame.mixer.quit()
pygame.quit()

