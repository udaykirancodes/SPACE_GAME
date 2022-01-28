import pygame
import random 
import math

from pygame import color 
# from pygame.constants import K_UP
# pygame initialising 
pygame.init()

# creating our first window 
screen = pygame.display.set_mode((800,600))

#title 
pygame.display.set_caption('My First Game')
# Icon
icon = pygame.image.load('images/twitter.png')
pygame.display.set_icon(icon)
# background color 

# Player 
playerImg = pygame.image.load('images/spaceship.png')
Default_player_size = (100,100)
playerImg = pygame.transform.scale(playerImg , Default_player_size)
playerX = 350
playerY = 480

#enemy

enemyImg = []
enemyX = []
enemyY= []
enemySpeedX = []
enemySpeedY = []
num_of_enemy = 5
enemyImage = pygame.image.load('images/1.png')
enemyImageResized = pygame.transform.scale(enemyImage,(50,50))
for i in range(num_of_enemy): 
    enemyX.append(random.randint(0,700))
    enemyY.append(random.randint(50,300))
    enemySpeedX.append(0.5)
    enemySpeedY.append(50)
    # enemyImg.append(pygame.image.load('images/1.png'))
    enemyImg.append(enemyImageResized)

#bullet 
bulletImg = pygame.image.load('images/bullet.png')
bulletSize = (30,30)
bulletImg = pygame.transform.scale(bulletImg,bulletSize)

bulletX = playerX+30
bulletY = playerY+30
bulletState = False
bulletSpeed = 1

# score_value = 0

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    for i in range(num_of_enemy):
        screen.blit(enemyImg[i] , (x,y))
def bullet(x,y,state):
    screen.blit(bulletImg , (x,y))
def isCollide(bulletX,bulletY,enemyX,enemyY): 
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY ,2)) 
    if(distance < 40 ):
        return True
    else:
        return False

def showScore(x,y):
    score = font.render("Score :  "+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    gameOverFont = pygame.font.Font('freesansbold.ttf',64)
    gameOverText = gameOverFont.render("GAME OVER",True,(255,255,255))
    screen.blit(gameOverText,(200,250))


playerChange = 20 
# enemySpeedX = .3
# enemySpeedY = 20

running = True
# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if a key stroke is pressed check whether left or right 
        if(event.type == pygame.KEYDOWN):        
            if (event.key == pygame.K_LEFT):
                if(playerX < 0):
                    playerX=0
                else:
                    playerX-=playerChange          
                # print('key')
            if(event.key == pygame.K_RIGHT):
                if(playerX>700):
                    playerX=700
                else:
                    playerX+=playerChange
                # print('key')
            
            #bullet movement 
            

            if(event.key == pygame.K_SPACE):
                bulletX = playerX +30 
                bulletY = playerY +30
                bulletState=True
                if(bulletState):
                    bullet(bulletX,bulletY,bulletState)
        # if(event.type == pygame.KEYUP): after pressed 
       
    # while the game is running 
    # enemy should move to the bottom 
    # enemyX += enemySpeedX 
    
   
    
    screen.fill((50,50,50))
    
    for i in range(num_of_enemy):
        # game Over 
        if enemyY[i] > 450:
            for j in range(num_of_enemy):
                enemyY[j]=2000
            game_over_text()
            break

        enemyX[i] += enemySpeedX[i]
        if (enemyX[i] <=0):
            enemyX[i]=0
            enemySpeedX[i] = 0.3
            enemyY[i]+=enemySpeedY[i]
            # 
        elif (enemyX[i]>=700):
            enemyX[i]=700
            enemySpeedX[i] = -0.3
            enemyY[i]+=enemySpeedY[i]
        elif (enemyY[i] >500):
            enemyY[i]=500

        collision = isCollide(bulletX,bulletY,enemyX[i],enemyY[i])
        if(collision):        
            bulletY = 480
            bulletState = False
            score_value+=1
            print(score_value)
            enemyX[i]  = random.randint(0,700)
            enemyY[i]  = random.randint(50,300)
        else:
            # print('Not Collided')
            pass
        
        enemy(enemyX[i],enemyY[i],i)
    #bullet movement 

    

    if(bulletState):
        bullet(bulletX,bulletY,bulletState)
        bulletY -= bulletSpeed

    if(bulletY <=0 ):
        bulletY=400
        bulletState=False

    player(playerX,playerY)
    # for i in range(num_of_enemy):
        # enemy(enemyX[i],enemyY[i],i)
    showScore(textX,textY)
    pygame.display.update()

