# -*- coding: utf-8 -*-
"""

@author: annak
"""
# -*- coding: utf-8 -*-
"""
AK-Anna Kelley's comments
RL-Rhea Lam's comments
VV - Vivian Vo's comments
"""


#AK-Import statement necessary to run the game
#RL- random and math are built-in python modules and pygame is a set of open-source python modules
import pygame
import random
import math

#RL-initializing pygame by calling pygame.init(), which sets up all modules part of pygame and prepares the environment for the code to run
pygame.init()

#AK-create the dimensions of the game screen in variables 
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,
                                  screen_height))


# Score

font = pygame.font.Font('freesansbold.ttf', 20)

levelScores=[10,25,40]
# Game Over
game_over_font = pygame.font.Font('freesansbold.ttf', 64)
playerImageUnscaled = pygame.image.load('spaceship.png')
playerImage=pygame.transform.scale(playerImageUnscaled,(100,100))
bombImage=pygame.image.load('bomb.png')
bombImage=pygame.transform.scale(bombImage,(30,30))
bulletImage = pygame.image.load('bullet.png')
bulletImage=pygame.transform.scale(bulletImage,(20,30))
background=pygame.image.load('background.jpg')
background=pygame.transform.scale(background,(800,600))

                
def levelComplete(level):
    text=game_over_font.render("Level " + str(level) + " Complete!", True, (255,255,255))
    screen.blit(text,(150,260))
    if level==1:
        textMessage=font.render("Watch out, the aliens are getting faster", True,(255,255,255) )
        screen.blit(textMessage,(200,400))
    elif level==2:
        textMessage=font.render("In level 3, don't hit the bombs!", True,(255,255,255) )
        screen.blit(textMessage,(230,400))
        
    pygame.display.update()
    
    pygame.time.delay(1000)
def show_score(x, y, score_val):
    score = font.render("Points: " + str(score_val),
                        True, (255,255,255))
    screen.blit(score, (x , y ))

def game_over():
    game_over_text = game_over_font.render("GAME OVER",
                                           True, (255,255,255))
    text=font.render("The game is over! If you would like to replay, press enter", True, (255,255,255))
    text2=font.render("If you would like to exit, press the X", True, (255,255,255))
    

    screen.blit(game_over_text, (190, 250))
    screen.blit(text, (105, 400))
    screen.blit(text2, (195, 450))
    pygame.display.update()
    pygame.time.delay(1000)
    enterKeyCheck=True
    while enterKeyCheck:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                enterKeyCheck=False
                return False

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                     enterKeyCheck=False
                     return True
    
def bombsCreate(no_of_bombs, bomb_Xchange, bomb_Ychange, bomb_X,bomb_Y, bombs):
    for num in range(no_of_bombs):
        bombs.append(bombImage)
        bomb_X.append(random.randint(60,737))
        bomb_Y.append(random.randint(50, 300))       
        bomb_Ychange.append(0)                        
        bomb_Xchange.append(random.uniform(0.3, 1)) 

def mainPlay():
    score_val = 0
    scoreX = 5
    scoreY = 5
    level=1
    player_X = 370
    player_Y = 490
    player_Xchange = 0
    explosion_X = 0
    explosion_Y = 0
    explosion_radius = 0
    explosion_active = False
    invaderImage = []
    invader_X = []
    invader_Y = []
    invader_Xchange = []
    invader_Ychange = []
    no_of_invaders = 8
    bombs=[]
    bomb_X=[]
    bomb_Y=[]
    bomb_Ychange=[]
    bomb_Xchange=[]
    bullet_X = 400
    bullet_Y = 490
    bullet_Ychange = 3
    bullet_state = "rest"
    
    for num in range(no_of_invaders):
        alienImg=pygame.image.load('alien.png')
        alienImg = pygame.transform.scale(alienImg, (40, 40))   
        invaderImage.append(alienImg)
        invader_X.append(random.randint(64, 737))
        invader_Y.append(random.randint(20, 160))
        invader_Xchange.append(0.6)
        invader_Ychange.append(50)
        
    
    running = True
    #AK start the game by using a while loop
    while running:
        if level>len(levelScores):
            
            return False
        #AK Fill the pygame screen with black

        screen.blit(background,(0,0))

        
        #AK this for loop looks at if the user decides to "quit" the game
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_Xchange = -1.7
                if event.key == pygame.K_RIGHT:
                    player_Xchange = 1.7
                if event.key == pygame.K_SPACE:
                  
                    if bullet_state == "rest":
                        bullet_X = player_X + 15
                        bullet_Y=player_Y
                        bullet_state=bullet(bullet_X, bullet_Y, bullet_state)
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    player_Xchange = 0

        if level <= len(levelScores) and score_val>=levelScores[level-1]:
            levelComplete(level)
            level+=1
            for i in range(no_of_invaders):
                invader_Xchange[i]+=0.3
                invader_Ychange[i]+=5
            if level==3:
                bombsCreate(5, bomb_Xchange, bomb_Ychange, bomb_X,bomb_Y, bombs)

        player_X += player_Xchange
        for i in range(no_of_invaders):
            invader_X[i] += invader_Xchange[i]

        if bullet_Y <= 0:
            bullet_Y = 600
            bullet_state = "rest"
        if bullet_state == "fire":
            bullet_state=bullet(bullet_X, bullet_Y,bullet_state)
            bullet_Y -= bullet_Ychange
        


        for i in range(no_of_invaders):
            
            if invader_Y[i] >= 450:
                if abs(player_X-invader_X[i]) < 80:
                    for j in range(no_of_invaders):
                        invader_Y[j] = 2000
                        
                    return False

            if invader_X[i] >= 735 or invader_X[i] <= 0:
                invader_Xchange[i] *= -1
                invader_Y[i] += invader_Ychange[i]
            # Collision
            collision = isCollision(bullet_X, invader_X[i],
                                    bullet_Y, invader_Y[i])
            if collision:
                score_val += 1
                bullet_Y = 600
                bullet_state = "rest"
                invader_X[i] = random.randint(64, 736)
                invader_Y[i] = random.randint(30, 200)
                invader_Xchange[i] *= -1

            invader(invader_X[i], invader_Y[i], i,invaderImage)

        
        if level>=2:
            for i in range(len(bombs)):
                bomb_Y[i]+=bomb_Ychange[i]
                bomb_X[i]+=bomb_Xchange[i]
                drawBomb(bomb_X[i], bomb_Y[i])
                if bomb_X[i]<=16 or bomb_X[i]>=750:
                    bomb_Xchange[i]*=-1
                drawBomb(bomb_X[i],bomb_Y[i])
                bombCollision=isCollision(bullet_X,bomb_X[i], bullet_Y, bomb_Y[i])
                gameOverExplosion = False
                if bombCollision and not gameOverExplosion:
                    explosion_X=bomb_X[i]
                    explosion_Y=bomb_Y[i]
                    explosion_radius=5 
                    explosion_active=True
                if explosion_active:
                    pygame.draw.circle(screen,(255,0,0), (int(explosion_X), int (explosion_Y)), explosion_radius)
                    explosion_radius+=1
                    if explosion_radius>=1000:
                        textMessage=game_over_font.render("You Hit a Bomb!", True,(255,255,255) )
                        screen.blit(textMessage,(140,250))
                        pygame.display.update()
                        pygame.time.delay(2000)
                        screen.fill((0,0,0))
                        pygame.display.update()
                        game_over()
                        return False
        if player_X <= 16:
            player_X = 16;
        elif player_X >= 750:
            player_X = 750
        
        player(player_X, player_Y)
        show_score(scoreX, scoreY, score_val)
        pygame.display.update()
    return True
    
#AK this function determines whether or not there is a collision between two object
#AK in this case it will be checking if the bullet "runs into" the alien
def isCollision(x1, x2, y1, y2):
    '''
    AK

    Parameters
    ----------
    x1 : Int
        x coordinate for first object
    x2 : Int
        x coordinate for second object
    y1 : Int
        y coordinate for first object
    y2 : Int
        y coordinate for second object

    Returns
    -------
    bool
        This will return true if the distance is within 50 pixels, or if the collision is detected
        It will return false if there is no collision detected and the two objects are not close enough

    '''
    '''AK the distance between the two is measured by squaring the 
    distance between each axis variable and then taking the square root of these 
    added together'''
    distance = math.sqrt((math.pow(x1 - x2,2)) +
                         (math.pow(y1 - y2,2)))
    #AK If the distance between the two is less or equal to 50, a colllision is detected
    if distance <= 30:
        return True
    else:
        return False

def player(x, y):
    screen.blit(playerImage, (x - 16, y + 10))

def invader(x, y, i, invaderImage):
    screen.blit(invaderImage[i], (x, y))

def bullet(x, y, bullet_state):
    screen.blit(bulletImage, (x, y))
    bullet_state = "fire"
    return bullet_state
def drawBomb(x,y):
    screen.blit(bombImage,(x,y))
run=True
while run:     
    mainPlay()
    replay=game_over()
    if not replay:
        pygame.quit()
        run=False
pygame.quit()
