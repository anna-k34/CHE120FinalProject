# -*- coding: utf-8 -*-
"""
AK-Anna Kelley's comments
RL-Rhea Lam's comments
VV-Vivian Vo's comments
NA- Naomi A's comments 
github username: anna-k34
"""


#AK-Import statement necessary to run the game
#RL- random and math are built-in python modules and pygame is a set of open-source python modules
#VV- pygame is for graphics, sounds and inputs. random is for alien positions (generate random numbers). math is for collision detection (math calculations).
#NA- random module is mainly used to position the aliens at random positions
import pygame
import random
import math

#RL-initializing pygame by calling pygame.init(), which sets up all modules part of pygame and prepares the environment for the code to run
#NA- One time setup call that gets pygame ready to draw on the screen
pygame.init()

#AK-create the dimensions of the game screen in variables 
screen_width = 800
screen_height = 600
#AK 
#VV- creates actual game window with dimesnsions defined above 
screen = pygame.display.set_mode((screen_width,
                                  screen_height))

# caption and icon
#VV- sets the title text in windows title bar
#AK create the screen using the width and height variables
screen = pygame.display.set_mode((screen_width,
                                  screen_height))

#AK the original creater set the label of the pygame screen 
pygame.display.set_caption("Welcome to Space\
Invaders Game by:- styles")



# Score
#VV - initializes player's score starting at 0
#NA- #NA- starts with the players score as zero this increases each time the player hits the alien with a blade 
score_val = 0
#VV - sets position where score is displayed (5 pixels from left, and 5 pixels top)
scoreX = 5
scoreY = 5

#VV - creates font object to display the player's score
font = pygame.font.Font('freesansbold.ttf', 20)

# Game Over
#VV - creates large font size for "game over" message

#AK create a new font for the regular text
font = pygame.font.Font('freesansbold.ttf', 20)

#AK create a new font to be used in the game over statement

game_over_font = pygame.font.Font('freesansbold.ttf', 64)

#VV - render() creates a text surface showing "Points:" and the current score value. True enables smooth text (anti-aliasing) and (255,255,255) is white colour code, blit() draws score text on the screen in position of (x,y)
def show_score(x, y):
    score = font.render("Points: " + str(score_val),
                        True, (255,255,255))
    screen.blit(score, (x , y ))
#VV - render() "game over" in white text (255,255,255 is the colour code) and displays it at (190,250) which is centre of screen
def game_over():
    game_over_text = game_over_font.render("GAME OVER",
                                           True, (255,255,255))
    screen.blit(game_over_text, (190, 250))

#VV - loads the spaceship image file and sizes it to 100x100 pixels
playerImageUnscaled = pygame.image.load('spaceship.png')
playerImage=pygame.transform.scale(playerImageUnscaled,(100,100))
#VV - sets the player position at 370 pixels from left (around centre) and 490 from top (close to bottom of screen)
player_X = 370
player_Y = 490
#VV - sets player's horizontal speed as 0 (not moving initially)
player_Xchange = 0

#VV - creates empty lists to store the alien's data (image, x and y position, and horizontal and vertical speed)
invaderImage = []
invader_X = []
invader_Y = []
invader_Xchange = []
invader_Ychange = []
#VV - sets number of aliens to 8
no_of_invaders = 8

#VV - for loop, loops 8 times to set up each alien
for num in range(no_of_invaders):
    alienImg=pygame.image.load('alien.png')
  #VV - loads and resizes aliens to 40x40 pixels and adds to list
    alienImg = pygame.transform.scale(alienImg, (40, 40))   
    invaderImage.append(alienImg)
  #VV - sets random starting positions for aliens (64-737 in x keeps within screen dimensions, and 30-180 y keeps aliens in top portion of screen)
    invader_X.append(random.randint(64, 737))
    invader_Y.append(random.randint(30, 180))
  #VV - sets movement speeds of aliens (horizontally: 0.6 pixels/frame, and vertically 50 drop distance when hit screen edge)
    invader_Xchange.append(0.6)
    invader_Ychange.append(50)

#VV - loads and resizes bullet image to 20x30 pixels
bulletImage = pygame.image.load('bullet.png')
bulletImage=pygame.transform.scale(bulletImage,(20,30))
#NA - sets bullets initial position at 0
bullet_X = 0
bullet_Y = 500
#VV - sets bullets horizontal movement speed at 0 (will shoot straight up) and vertical speed at 3 pixels per frame upward
bullet_Xchange = 0
bullet_Ychange = 3
#VV - tracks whether bullet is currently moving ("fire") or ready to shoot ("rest")
bullet_state = "rest"

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
    #AkIf the distance between the two is less or equal to 50, a colllision is detected
    if distance <= 50:
        return True
    else:
        return False

def player(x, y):
    screen.blit(playerImage, (x - 16, y + 10))

def invader(x, y, i):
    screen.blit(invaderImage[i], (x, y))

def bullet(x, y):
    global bullet_state
    screen.blit(bulletImage, (x, y))
    bullet_state = "fire"
#AK track the game state by using a booean variabl
running = True
#AK start the game by using a while loop that looks at the boolean var
while running:

    #AK Fill the pygame screen with black
    screen.fill((0, 0, 0))
    
    #AK This for loop tracks the user's "events with the keyboard. Basically it looks for if they press a key or click a button
    #AK It checks each event the user does and compares it with the event type's inside of the for loop to see if they match
    for event in pygame.event.get():
        #AK this if looks at if the user decides to "quit" the game-The event test looks for if they press the X button on the pygame display
        if event.type == pygame.QUIT:
            #AK if the user presses the exit button quit this running loop so the game can end
            running = False
        #AK this if statement looks at if the user clicks certain buttons to move the spaceship or fire a bullet
        if event.type == pygame.KEYDOWN:
            #AK this statement checks if the user clicked the left arrow, and moves spaceship left as a result by changing its X change var
            if event.key == pygame.K_LEFT:
                player_Xchange = -1.7
            #AK this statement checks if the user clicked the right arrow, and moves spaceship right as a result by adjusting its X change var
            if event.key == pygame.K_RIGHT:
                player_Xchange = 1.7
            #AK this statement checks if the user clicked on the space key, which in turn will fire the bullet at the invaders
            if event.key == pygame.K_SPACE:
                #NA this if statement checks if they already have an active button, can't click the space button twice
                if bullet_state == "rest":
                    #Sets the bullet x variable to where the invader is so it can fire from the player's position
                    bullet_X = player_X
                    #This calls the bullet function to create a bullet
                    bullet(bullet_X, bullet_Y)
        #AK this statement just makes sure the spaceship doesn't move infinitely-if the user releases the key then the spaceship stops moving
        if event.type == pygame.KEYUP:
            #AK set the player's x change var to 0 so it will stop moving
            player_Xchange = 0

    #AK update the spaceship's position using the player x change variable
    player_X += player_Xchange
    for i in range(no_of_invaders):
        invader_X[i] += invader_Xchange[i]
    #VV - if bullet reaches top of screen, reset it back to bottom of screen and set the state back to "rest" so it can be fired again
    if bullet_Y <= 0:
        bullet_Y = 600
        bullet_state = "rest"
    #VV - if bullet is currently fired (in movement), draw it at its current position and move it upward by subtracting bullet_Ychange
    if bullet_state == "fire":
        bullet(bullet_X, bullet_Y)
        bullet_Y -= bullet_Ychange

#VV - for loop, loop through each of the 8 aliens
    for i in range(no_of_invaders):
        #VV - if alien is vertically within y of 450 pixels (near player level), check how close the alien is horizontally (and if within 80 pixels)
        if invader_Y[i] >= 450:
          #VV - abs() ensures the distance between is positive, and if the distance between the player and alien is less than 80, move all aliens off the screen (Y=20005)
            if abs(player_X-invader_X[i]) < 80:
                for j in range(no_of_invaders):
                    invader_Y[j] = 20005
                #VV - display "game over" message and exit the alien loop
                game_over()
                break
        #NA - if the alien hits the right edge (x is more or equal to 735) or left edge (x is less or equal to 0), then reverse its horizontal direction (multiply speed by -1) to make the alien "bounce" off the side and move the alien down by 50 pixels
        if invader_X[i] >= 735 or invader_X[i] <= 0:
            invader_Xchange[i] *= -1
            invader_Y[i] += invader_Ychange[i]
        # Collision
      #VV - check if bullet has collided with alien
        collision = isCollision(bullet_X, invader_X[i],
                                bullet_Y, invader_Y[i])
      #VV - if collision is detected (bullet hits alien), increase score by 1
        if collision:
            score_val += 1
            bullet_Y = 600
          #VV - reset the bullet to the bottom of the screen and set state to "rest"
            bullet_state = "rest"
          #NA - respawn the hit/collided alien at a new random position at the top of the screen
            invader_X[i] = random.randint(64, 736)
            invader_Y[i] = random.randint(30, 200)
            invader_Xchange[i] *= -1
        #VV - draw the current alien at updated position
        invader(invader_X[i], invader_Y[i], i)


#VV - ensures the player cannot go off the screen (keeps within screen dimension boundaries)
    if player_X <= 16:
        player_X = 16;
    elif player_X >= 750:
        player_X = 750

#VV - draw the player spaceship at its current position
    player(player_X, player_Y)
  #VV - displays the player's score on screen
    show_score(scoreX, scoreY)
    pygame.display.update()
#VV - when game loop ends, closes pygame
pygame.quit()
