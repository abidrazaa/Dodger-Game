import random
import pygame
pygame.init()
win=pygame.display.set_mode((700,480))
pygame.display.set_caption('DODGER')
music=pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

                          
bg = pygame.image.load('background.png')
char=pygame.image.load('standing.png')
image=pygame.image.load('balls.png')

clock=pygame.time.Clock()
x=450 
y=450
vel=8
f=255
o=0
b=255
r=255
e=0
t=255
yaxis=-100
xaxis=random.randrange(0,600)
yAxis=-100
xAxis= random.randrange(0,600)
Xaxis=random.randrange(0,600)
Yaxis=-100
j=80
gameExit = False
xMan = 40
n=20
font = pygame.font.SysFont(None, 40)
newfont=pygame.font.SysFont(None,40)
score=0
bonus=0
totalscore=score+bonus


def game_over():
    win=pygame.display.set_mode((700,500))
    win.fill((255,0,255))
    largeText=pygame.font.SysFont(None,60)
    Text=largeText.render('GameOver!',20,(0,0,0))
    text=largeText.render("score: "+str(score+bonus),20,(0,0,0))
    win.blit(Text,(230,200))
    win.blit(text,(230,260))
    pygame.display.update()


def movingMan(xMan):
    win.blit(char,(xMan,420))
   
    

def redrawGameWindow():
    win.blit(bg,(0,0))
  
    Text = font.render("Dodged: " +str(score), 5, (255,255,255))
    newtext=newfont.render("Bonus:" +str(bonus),5,(255,255,255))
    win.blit(newtext,(565,0))
    win.blit(Text,(0,0))
    

def bonus_point(Xaxis,Yaxis):
    win.blit(image,(Xaxis,Yaxis))
   # pygame.display.update()
    

def controllingSquare(xAxis,yAxis):   
    pygame.draw.rect(win,(f,o,b),[xAxis,yAxis,n,40])
        
def new_Square(xaxis,yaxis):
    
    pygame.draw.rect(win,(e,r,t),[xaxis,yaxis,j,40])


while not gameExit:
    
    clock.tick(27)
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            gameExit ==True
            quit()
    if keys[pygame.K_LEFT] and xMan>0 or keys[pygame.K_a] and xMan>0:
        xMan-=vel
    elif keys[pygame.K_RIGHT] and xMan<650 or keys[pygame.K_d]and xMan<650:
        xMan+=vel



    if yAxis>480:
        
        f=random.randint(0,255)
        o=random.randint(0,255)
        b=random.randint(0,255)
        #n=random.randrange(20,100)
        score=score+1
        yAxis = -100
        xAxis=random.randrange(0,600)
        
    if yaxis>480:
        e=random.randint(0,255)
        r=random.randint(0,255)
        t=random.randint(0,255)
        #j=random.randrange(20,100)
        score=score+1
        yaxis = -100
        xaxis=random.randrange(0,600)
        
    if (xAxis<xMan+ 50) and xAxis+n > xMan+15 and (yAxis+20>420):
        game_over()
        gameExit=True 
        quit()
      
    if (xaxis < xMan+50) and (xaxis+j >xMan + 15) and (yaxis+20)>420:
        game_over()
        gameExit=True
        quit()
        
        

    if score>=2:
        bonus_point(Xaxis,Yaxis)
        Yaxis=Yaxis+5
   
        
    if (Xaxis<xMan+50) and (Xaxis+112>xMan+15) and (Yaxis+56>420)and (Yaxis+56<480):
        bonus=bonus+2
        Yaxis=-100
        Xaxis=-100
    if Yaxis>480 and score%12==0:
        Yaxis=-100
        Xaxis=random.randrange(0,600)
        

    if Yaxis>480:
        YAxis=-100
        Xaxis=random.randrange(0,600)
       
        

    if score>=2 and score<50:
        l=random.randrange(10,12)
        p=random.randrange(10,12)
        yaxis=yaxis+10
        
    if score<50:
        yAxis=yAxis+12
    elif score>=20 and score<30:
        p=random.randrange(20,30)
        yAxis=yAxis+p
        
        l=random.randrange(10,20)
        yaxis=yaxis+l
        
    elif score>=30:
        p=random.randrange(25,35)
        yAxis=yAxis+p
        
        l=random.randrange(10,20)
        yaxis=yaxis+1
        
    if yaxis < 0:
        if (xaxis < xAxis+n and xaxis+j > xAxis ):
            xaxis = random.randrange(0,600)
    if yAxis < 0:
        if  (xAxis < xaxis+j and xAxis+n > xaxis ):
            xAxis = random.randrange(0,600)

    redrawGameWindow()
    bonus_point(Xaxis,Yaxis)
    new_Square(xaxis,yaxis)
    controllingSquare(xAxis,yAxis)
    movingMan(xMan)
    pygame.display.update()
   



    
