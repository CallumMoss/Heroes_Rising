import simplegui
import random
import time
from user304_rsf8mD0BOQ_1 import Vector

class GameConstants:
    #constants in our game that dont change an we will be using throughout our code
        SAMURAI_SPRITE_SHEET = simplegui.load_image('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/samuraiSpriteSheet.png')
        MAGE_SPRITE_SHEET = simplegui.load_image('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/mageSpriteSheet.png')
        MAGE_RED_SPRITE_SHEET = simplegui.load_image('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/mageRedSpriteSheet.png')
        FOOT_SOLDIER_SPRITE_SHEET = simplegui.load_image('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/footSoldierSpriteSheet.png')
        FOOT_SOLDIER_BLUE_SPRITE_SHEET = simplegui.load_image('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/footSoldierBlueSpriteSheet.png')
        FIRE_BALL_SPRITE_SHEET = simplegui.load_image('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/fireballSpriteSheet.png')
        
        BACKGROUND_IMAGE = simplegui.load_image('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/background.png')
        BACKGROUND_AFTERNOON_IMAGE = simplegui.load_image('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/backgroundAfternoon.png')
        BACKGROUND_NIGHT_IMAGE = simplegui.load_image('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/backgroundNight.png')
        
        SAMURAI_CONTROLS = simplegui.load_image('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/samuraiControlsImage.png')
        MAGE_CONTROLS = simplegui.load_image('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/mageControlsImage.png')
        
        #-------------------- Canvas dimensions
        
        WIDTH = 800 # 16 * 50
        HEIGHT = 450 # 9 * 50
        
        #-------------------- Background Image Dimensions
        
        BACKGROUND_WIDTH = 1274
        BACKGROUND_HEIGHT = 690
        
        #-------------------- Heart images
        
        FULL_HEART_IMAGE = simplegui.load_image('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/fullHeart.png')
        HALF_HEART_IMAGE = simplegui.load_image('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/halfHeart.png')
        EMPTY_HEART_IMAGE = simplegui.load_image('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/emptyHeart.png')
        
        #-------------------- Initialising player sprite dimensions
        
        IMG_DIMS = 256
        SPRITE_SIZE = 128
        
        #-------------------- Initialising sounds
        
        WELCOME_SCREEN_MUSIC = simplegui.load_sound('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/luka1.mp3')
        GENERAL_MUSIC = simplegui.load_sound('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/wanoTheme.mp3')
        MAGE_LIGHTATK = simplegui.load_sound('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/mageLightAttack')
        MAGE_HEAVYATK = simplegui.load_sound('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/mageHeavyAttack')
        SAMURAI_LIGHTATK = simplegui.load_sound('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/samuraiLightAttack.mp3')
        SAMURAI_HEAVYATK  = simplegui.load_sound('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/samuraiHeavyAttack')
        VICTORYSFX = simplegui.load_sound('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/victorySoundEffect')
        GAMEOVERSFX = simplegui.load_sound('https://www.cs.rhul.ac.uk/home/zlac354/HeroesRisingAssets/gameOverSoundEffect')
        
        #-------------------- Initialising game initialisation variables
        
        CHAR_SELECTED = ""
        
        # GAME STATE : (0 - GameOver, 1 - Start / Welcome Screen, 2 - Running / Main Game, 3 - Victory Screen)
        GAME_STATE = 1 #using game states to help reset audio and game
        SCREEN = 0

class StartGame:
    def __init__(self):#initalizing for menu and character backstories, including controls
        self.storyTextSamurai = "A ruthless mage and his ashigaru (foot soldiers) \nhave invaded the kingdom of Zano. \nYour mission, as the kingdom's\ngreatest samurai, and last hope,\nis to take down the evil mage\nand restore the Shogun back\nto the throne."
        self.storyTextMage = "A ruthless samurai and his ashigaru (foot soldiers) \nhave invaded the kingdom of Zano. \nYour mission, as the kingdom's\ngreatest mage, and last hope,\nis to take down the evil mage\nand restore the Shogun back\nto the throne."
        
        self.buttonSize = 50
        #using GameConstants class to get the predetermined variables
        self.button_pos1 = [(GameConstants.WIDTH/2 - self.buttonSize - 100, GameConstants.HEIGHT/2 - self.buttonSize/2),
                         (GameConstants.WIDTH/2 - self.buttonSize + self.buttonSize + 100, GameConstants.HEIGHT/2 - self.buttonSize/2 ),
                         (GameConstants.WIDTH/2 - self.buttonSize + self.buttonSize + 100, GameConstants.HEIGHT/2 - self.buttonSize/2 + self.buttonSize),
                         (GameConstants.WIDTH/2 - self.buttonSize - 100, GameConstants.HEIGHT/2 - self.buttonSize/2 + self.buttonSize)]
        self.button_text_pos1 = (GameConstants.WIDTH/2 - self.buttonSize - 65, GameConstants.HEIGHT/2 - self.buttonSize + self.buttonSize + 10 )
        #initialising text for menu screen
        self.button_text_name = "BEGIN GAME"
        self.subheading_text = "Avenge Your Fallen Kingdom!"
        self.character_text_size1 = 0
        self.character_text_size2 = 0
        
        
        self.image_1_center_source = (128, 128) 
        self.image_1_wh_source = (256, 256)
        self.image_1_center_destination = (GameConstants.WIDTH/4 + 100, GameConstants.HEIGHT/2)
        self.image_1_wh_destination = (0.1, 0.1)
        
        self.image_2_center_source = (128, 128) 
        self.image_2_wh_source = (256, 256)
        self.image_2_center_destination = (GameConstants.WIDTH/4 + 300, GameConstants.HEIGHT/2 )
        self.image_2_wh_destination = (0.1, 0.1)
                          
        self.image1 = GameConstants.SAMURAI_SPRITE_SHEET
        self.image2 = GameConstants.MAGE_SPRITE_SHEET
        
      #-------------------------------------------------------------------------------------------------------

   # SHIFTED THE EVENT HANDLER CODE WHICH WAS HERE, AT THE BOTTOM.
    
   # CREATED game_reset FUNCTION - WHICH IS USE TO RESET THE STARTING FRAME RESOURCES. 
           
   #-------------------------------------------------------------------------------------------------------
    
    def game_reset(self): #this method resets the game, looping everything together once playagain is pressed
        GameConstants.SCREEN = 0
        self.button_size = 50
        self.button_pos1 = [(GameConstants.WIDTH/2 - self.button_size - 100, GameConstants.HEIGHT/2 - self.button_size/2),
                         (GameConstants.WIDTH/2 - self.button_size + self.button_size + 100, GameConstants.HEIGHT/2 - self.button_size/2 ),
                         (GameConstants.WIDTH/2 - self.button_size + self.button_size + 100, GameConstants.HEIGHT/2 - self.button_size/2 + self.button_size),
                         (GameConstants.WIDTH/2 - self.button_size - 100, GameConstants.HEIGHT/2 - self.button_size/2 + self.button_size)]
        self.button_text_pos1 = (GameConstants.WIDTH/2 - self.button_size - 65, GameConstants.HEIGHT/2 - self.button_size + self.button_size + 10 )
        self.button_text_name = "BEGIN GAME"
        self.subheading_text = "Avenge Your Fallen Kingdom!"
        self.character_text_size1 = 0
        self.character_text_size2 = 0
        
        
        self.image_1_center_source = (128, 128) 
        self.image_1_wh_source = (256, 256)
        self.image_1_center_destination = (GameConstants.WIDTH/4 + 100, GameConstants.HEIGHT/2)
        self.image_1_wh_destination = (0.1, 0.1)
        
        self.image_2_center_source = (128, 128) 
        self.image_2_wh_source = (256, 256)
        self.image_2_center_destination = (GameConstants.WIDTH/4 + 300, GameConstants.HEIGHT/2 )
        self.image_2_wh_destination = (0.1, 0.1)
        
                    
        self.image1 = GameConstants.SAMURAI_SPRITE_SHEET
        self.image2 = GameConstants.MAGE_SPRITE_SHEET

    def show_storyboard(self): #displays character controls and backstorys
        GameConstants.SCREEN += 1
        #self.frame += 1
        StartGame.set_character_text(self, False)
        
        if GameConstants.CHAR_SELECTED == "Samurai": #branching used to display each characters unique story
            self.image2 = GameConstants.SAMURAI_CONTROLS
            self.image_1_center_destination = (GameConstants.WIDTH/4, GameConstants.HEIGHT/2)
            self.image_2_center_source = (self.image2.get_width()//2, self.image2.get_height()//2)
            self.image_2_wh_source = (self.image2.get_width(), self.image2.get_height())
            self.image_2_center_destination = (GameConstants.WIDTH/2 - 100, GameConstants.HEIGHT - 70)
            self.image_2_wh_destination = (self.image2.get_width() // 1.75, self.image2.get_height() // 1.75)
            
        else:
            self.image1 = GameConstants.MAGE_CONTROLS
            self.image_2_center_destination = (GameConstants.WIDTH/4, GameConstants.HEIGHT/2)
            self.image_1_center_source = (self.image1.get_width()//2, self.image1.get_height() // 2)
            self.image_1_wh_source = (self.image1.get_width(), self.image1.get_height())
            self.image_1_center_destination = (GameConstants.WIDTH/2 - 100, GameConstants.HEIGHT - 70)
            self.image_1_wh_destination = (self.image1.get_width() // 1.75, self.image1.get_height() // 1.75)
            
        StartGame.set_subheading(self, "Character's Story & Controls")
        self.button_pos1 = [(GameConstants.WIDTH - self.buttonSize - 120, GameConstants.HEIGHT - self.buttonSize - 20),
                            (GameConstants.WIDTH - 20, GameConstants.HEIGHT - self.buttonSize - 20),
                            (GameConstants.WIDTH - 20, GameConstants.HEIGHT - 20),
                            (GameConstants.WIDTH - self.buttonSize - 120, GameConstants.HEIGHT - 20)] 
        self.button_text_pos1 = (GameConstants.WIDTH - 130, GameConstants.HEIGHT - 35)
            

    def set_subheading(self, text):
        self.subheading_text = text
    
    def set_character_text(self, text_state):
        if text_state:
            self.character_text_size1 = 25
            self.character_text_size2 = 25
        else:
            self.character_text_size1 = 0
            self.character_text_size2 = 0

    def set_image1(self):
        self.image_1_wh_destination = (95 *1.75 ,93 *1.75)

    def set_image2(self):
        self.image_2_wh_destination = (95 *1.75 ,93 *1.75)
        
    def set_button(self):
        GameConstants.SCREEN += 1
        #self.frame += 1
        self.button_text_name = "NEXT" 
        self.button_pos1 = [(0, 0),
                            (0, 0),
                            (0, 0),
                            (0, 0)] 
        self.button_text_pos1 = (GameConstants.WIDTH + 100, GameConstants.HEIGHT + 100)
        
        StartGame.set_subheading(self, "Select the Character To Play")
        StartGame.set_character_text(self, True)
        StartGame.set_image1(self)
        StartGame.set_image2(self)

    #-------------------------------------------------------------------------------------------------------
    
    def draw(self, canvas): #brings all the previous methods together and draws the menu/character selection page.
        canvas.draw_image(GameConstants.BACKGROUND_IMAGE, (GameConstants.BACKGROUND_WIDTH//2, GameConstants.BACKGROUND_HEIGHT//2),
                                      (GameConstants.BACKGROUND_WIDTH, GameConstants.BACKGROUND_HEIGHT), 
                                      (GameConstants.WIDTH/2, GameConstants.HEIGHT/2), 
                                      (GameConstants.WIDTH, GameConstants.HEIGHT))
        
        canvas.draw_image(self.image1, 
                          self.image_1_center_source, 
                          self.image_1_wh_source, 
                          self.image_1_center_destination, 
                          self.image_1_wh_destination)
        
        canvas.draw_image(self.image2, 
                          self.image_2_center_source, 
                          self.image_2_wh_source, 
                          self.image_2_center_destination, 
                          self.image_2_wh_destination)
        
        canvas.draw_text("MAGE", (GameConstants.WIDTH/4 + 260, GameConstants.HEIGHT/2 + 120), self.character_text_size1 , "white", "monospace")
        
        canvas.draw_text("SAMURAI", (GameConstants.WIDTH/4 + 50, GameConstants.HEIGHT/2 + 120), self.character_text_size2 , "white", "monospace")
        
        canvas.draw_text(self.subheading_text, (GameConstants.WIDTH/2 - 150, GameConstants.HEIGHT/2 - 100), 20, "white", "monospace")

        canvas.draw_polygon(self.button_pos1, int(self.buttonSize/10) , 
                            "#d9d9d9", 
                            "#bebfbe") 


        # draw text on next button
        canvas.draw_text(self.button_text_name, self.button_text_pos1 ,int(self.buttonSize/1.5) , "black", "monospace")

        # draw text of HEROES RISING
        canvas.draw_text("HEROES RISING", (GameConstants.WIDTH/2 - 300, GameConstants.HEIGHT/2 - 150), 80, "white", "monospace")
        
        #--------------------------------------------------------------------------------------------
        # Printing Story
        #--------------------------------------------------------------------------------------------
        
        if GameConstants.SCREEN == 2:
            if GameConstants.CHAR_SELECTED == "Samurai":
                lines = self.storyTextSamurai.split("\n")
            else:
                lines = self.storyTextMage.split("\n")
            
            line_height = 20
            for i in range(len(lines)):
                canvas.draw_text(lines[i], (GameConstants.WIDTH/2 - 50, GameConstants.HEIGHT/4 + 50 + i * line_height), 15, "white", "monospace")
                
        #--------------------------------------------------------------------------------------------
class EndGame:#class for gameover page
    def __init__(self):
        self.button_size = 50
        self.button_pos1 = [(GameConstants.WIDTH/2 - self.button_size - 100, GameConstants.HEIGHT/2 - self.button_size/2),
                         (GameConstants.WIDTH/2 - self.button_size + self.button_size + 100, GameConstants.HEIGHT/2 - self.button_size/2 ),
                         (GameConstants.WIDTH/2 - self.button_size + self.button_size + 100, GameConstants.HEIGHT/2 - self.button_size/2 + self.button_size),
                         (GameConstants.WIDTH/2 - self.button_size - 100, GameConstants.HEIGHT/2 - self.button_size/2 + self.button_size)]
        self.button_text_pos1 = (GameConstants.WIDTH/2 - self.button_size - 65, GameConstants.HEIGHT/2 - self.button_size + self.button_size + 10 )
        self.button_text_name = "PLAY AGAIN"
        self.start = StartGame()   

    def draw(self,canvas): # draws gameover page once called upon using the declared objects above
        canvas.draw_image(GameConstants.BACKGROUND_NIGHT_IMAGE, (637,345),(1274, 690), (GameConstants.WIDTH/2, GameConstants.HEIGHT/2), (GameConstants.WIDTH, GameConstants.HEIGHT))

        canvas.draw_polygon(self.button_pos1, int(self.button_size/10) , "#d9d9d9", "#bebfbe") 
        canvas.draw_text("Buckle Up, Let's Play Again", (GameConstants.WIDTH/2 - 170, GameConstants.HEIGHT - 60), 20, "white", "monospace")

        # draw text on next button
        canvas.draw_text(self.button_text_name, self.button_text_pos1 ,int(self.button_size/1.5) , "black", "monospace")

        # draw text of HEROES RISING
        ############################
        GameConstants.GENERAL_MUSIC.pause() #pauses the main theme ost of the game
        canvas.draw_text("GAME OVER", (GameConstants.WIDTH/2 - 250, GameConstants.HEIGHT/2 - 70), 100, "#ef3e15", "monospace")

class Victory: #victory screen class
    def __init__(self, character):
        self.character = character
        self.button_size = 50
        self.button_pos1 = [(GameConstants.WIDTH/2 - self.button_size - 100, GameConstants.HEIGHT/2 - self.button_size/2),
                         (GameConstants.WIDTH/2 - self.button_size + self.button_size + 100, GameConstants.HEIGHT/2 - self.button_size/2 ),
                         (GameConstants.WIDTH/2 - self.button_size + self.button_size + 100, GameConstants.HEIGHT/2 - self.button_size/2 + self.button_size),
                         (GameConstants.WIDTH/2 - self.button_size - 100, GameConstants.HEIGHT/2 - self.button_size/2 + self.button_size)]
        self.button_text_pos1 = (GameConstants.WIDTH/2 - self.button_size - 65, GameConstants.HEIGHT/2 - self.button_size + self.button_size + 10 )
        self.button_text_name = "PLAY AGAIN"
        self.start = StartGame()   #initalizes the StartGame method so that it can be called once playgame is pressed

    def draw(self, canvas):#draws victory screen when needed
        canvas.draw_image(GameConstants.BACKGROUND_NIGHT_IMAGE, (637,345),(1274, 690), (GameConstants.WIDTH/2, GameConstants.HEIGHT/2), (GameConstants.WIDTH, GameConstants.HEIGHT))

        canvas.draw_polygon(self.button_pos1, int(self.button_size/10) , "#d9d9d9", "#bebfbe") 
        canvas.draw_text(">> Congrats! You have restored the Shogun back to the throne! <<", (GameConstants.WIDTH/2 - 330, GameConstants.HEIGHT - 60), 20, "white", "monospace")
        canvas.draw_text("Score: " + str(self.character.score), (GameConstants.WIDTH/2 - 90, GameConstants.HEIGHT - 80), 20, "white", "monospace") # displays final score
        
        # draw text on next button
        canvas.draw_text(self.button_text_name, self.button_text_pos1 ,int(self.button_size/1.5) , "black", "monospace")

        # draw text of HEROES RISING
        GameConstants.GENERAL_MUSIC.pause() #pauses general music to allow victory music to play.
        ###########################
        canvas.draw_text("VICTORY!", (GameConstants.WIDTH/2 - 220, GameConstants.HEIGHT/2 - 70), 100, "yellow", "monospace")

# Centre of each square on sprite sheet 128, 384, 640, 896, 1152, 1408, 1664, 1920
# Each square dimensions 256, 256 
# Background: 1274, 690
# fireball sprite sheet: 110 x 110, starts at 55 --> 165 --> 275

class Player: # Player/character Class
    def __init__(self, image, footSoldierRight, footSoldierLeft, keyboard, isMage):
        self.img_centre = (GameConstants.IMG_DIMS/2, GameConstants.IMG_DIMS/2)
        self.img_dest_dim = (GameConstants.SPRITE_SIZE, GameConstants.SPRITE_SIZE)
        self.IMG = image
        self.hitbox = 32
        self.position = (Vector(GameConstants.WIDTH / 2, GameConstants.HEIGHT - 64))
        self.vel = Vector()
                
        self.footSoldierRight = footSoldierRight
        self.footSoldierRightImage = GameConstants.FOOT_SOLDIER_SPRITE_SHEET
        self.footSoldierLeft = footSoldierLeft
        self.isMage = isMage
        self.footSoldierRight_img_dest_dim = 128, 128
        self.footSoldierRight_hitbox = 64
        
        self.fireball = Fireball(self)
        self.background = Background(self)
        self.keyboard = keyboard
        
        self.inContactRight = False
        self.inContactLeft = False
        
        self.backgroundImage = GameConstants.BACKGROUND_IMAGE
        
        self.hearts = [GameConstants.FULL_HEART_IMAGE, GameConstants.FULL_HEART_IMAGE, GameConstants.FULL_HEART_IMAGE,
                        GameConstants.FULL_HEART_IMAGE, GameConstants.FULL_HEART_IMAGE, GameConstants.FULL_HEART_IMAGE,
                            GameConstants.FULL_HEART_IMAGE, GameConstants.FULL_HEART_IMAGE, GameConstants.FULL_HEART_IMAGE,
                                GameConstants.FULL_HEART_IMAGE]
        self.score = 0
        
        self.miniBossTimer = 60
        self.miniBossTimerIterator = 0
        self.bossTimer = 120
        self.bossTimerIterator = 0

    def draw(self, canvas):
        self.background.draw(canvas, self.backgroundImage)
        #draws background
        canvas.draw_image(self.IMG, self.img_centre, (GameConstants.IMG_DIMS, GameConstants.IMG_DIMS), (self.position.x, self.position.y), self.img_dest_dim)
        #draws sprite
        if self.bossTimer <= 0:
            canvas.draw_text("Score: " + str(self.score), [GameConstants.WIDTH - 150, 30], 20, 'white', 'monospace')
        else:
            canvas.draw_text("Score: " + str(self.score), [GameConstants.WIDTH - 150, 60], 20, 'white', 'monospace')
        # draws score
        self.fireball.draw(canvas)
        #draws fireball
        self.footSoldierRight.draw(canvas, self.footSoldierRightImage, self.footSoldierRight_img_dest_dim, self.footSoldierRight_hitbox)
        #draws right footsoldier
        self.footSoldierLeft.draw(canvas, GameConstants.FOOT_SOLDIER_SPRITE_SHEET, (128,128), 64)
        #draws left footsoldier
        if self.miniBossTimerIterator == 60:
            self.miniBossTimerIterator = 0
            self.miniBossTimer -= 1
            
        if self.bossTimerIterator == 60:
            self.bossTimerIterator = 0
            self.bossTimer -= 1
            
        if self.miniBossTimer <= 0:
            if self.isMage and self.bossTimer >= 0:
                canvas.draw_text("Samurai arrives in: " + str(self.bossTimer), (GameConstants.WIDTH - 250, 30), 20, "red", "monospace")
            elif self.bossTimer >= 0:
                canvas.draw_text("Mage arrives in: " + str(self.bossTimer), (GameConstants.WIDTH - 250, 30), 20, "red", "monospace")
        else:
            canvas.draw_text("Mini-Boss arrives in: " + str(self.miniBossTimer), (GameConstants.WIDTH - 280, 30), 20, "red", "monospace")
       
        canvas.draw_image(self.hearts[0], (341/2, 341/2), (341,341), (30, 30), (30,30))
        canvas.draw_image(self.hearts[1], (341/2, 341/2), (341,341), (55, 30), (30,30))
        canvas.draw_image(self.hearts[2], (341/2, 341/2), (341,341), (80, 30), (30,30))
        canvas.draw_image(self.hearts[3], (341/2, 341/2), (341,341), (105, 30), (30,30))      
        canvas.draw_image(self.hearts[4], (341/2, 341/2), (341,341), (130, 30), (30,30))
        canvas.draw_image(self.hearts[5], (341/2, 341/2), (341,341), (155, 30), (30,30))
        if self.isMage == False:
            canvas.draw_image(self.hearts[6], (341/2, 341/2), (341,341), (180, 30), (30,30))
            canvas.draw_image(self.hearts[7], (341/2, 341/2), (341,341), (205, 30), (30,30))
            canvas.draw_image(self.hearts[8], (341/2, 341/2), (341,341), (230, 30), (30,30))
            canvas.draw_image(self.hearts[9], (341/2, 341/2), (341,341), (255, 30), (30,30))
            
        for i in range (10):
            self.hearts[i] = GameConstants.FULL_HEART_IMAGE
            
        self.miniBossTimerIterator += 1
        self.bossTimerIterator += 1
        
    def update(self):
        self.position.add(self.vel)
        self.vel.multiply(0.85)
        
class FootSoldier:
    
    # Initializing the FootSoldier and Position Parameters
    
    def __init__(self, image, rightSide):
        self.rightSide = rightSide
        self.img_centre = (GameConstants.IMG_DIMS/2, GameConstants.IMG_DIMS/2)
        self.hitbox = (GameConstants.SPRITE_SIZE/2)
        if self.rightSide:
            self.position = (Vector(GameConstants.WIDTH + random.randint(self.hitbox, self.hitbox * 10), GameConstants.HEIGHT - self.hitbox))
        else:
            self.position = (Vector(0 - random.randint(self.hitbox, self.hitbox * 10), GameConstants.HEIGHT - self.hitbox))
        self.vel = Vector()
         
    def update(self): 
        self.position.add(self.vel)
        self.vel.multiply(0.85)
        
    # Drawing the foot soldie on the canvas
    
    def draw(self, canvas, image, img_dest_dim, hitbox):
        if self.rightSide:
            self.position = (Vector(self.position.x, GameConstants.HEIGHT - hitbox))
        canvas.draw_image(image, self.img_centre, (GameConstants.IMG_DIMS, GameConstants.IMG_DIMS), (self.position.x, self.position.y), img_dest_dim)
        
class Background:

    def __init__(self, character):
        self.character = character
        self.xPosition = GameConstants.WIDTH/2

    def update(self, canvas):
        if self.character.inContactRight == False:
            if self.character.keyboard.right and self.character.keyboard.rightDown:
                self.xPosition -= 2
            if self.xPosition == -(GameConstants.WIDTH/2):
                self.xPosition = GameConstants.WIDTH/2
        if self.character.inContactLeft == False:
            if self.character.keyboard.left and self.character.keyboard.leftDown:
                self.xPosition += 2
            if self.xPosition == (GameConstants.WIDTH/2): 
                self.xPosition = -(GameConstants.WIDTH/2)
                
    def draw(self, canvas, image):
        canvas.draw_image(image,(637,345), (1274, 690), (self.xPosition - GameConstants.WIDTH, GameConstants.HEIGHT/2), (GameConstants.WIDTH, GameConstants.HEIGHT))
        canvas.draw_image(image,(637,345), (1274, 690), (self.xPosition, GameConstants.HEIGHT/2), (GameConstants.WIDTH, GameConstants.HEIGHT))
        canvas.draw_image(image,(637,345), (1274, 690), (self.xPosition + GameConstants.WIDTH, GameConstants.HEIGHT/2), (GameConstants.WIDTH, GameConstants.HEIGHT))
            
        # draws to images back to back images
        if self.xPosition == -(GameConstants.WIDTH/2): # half of image width
            self.xPosition = GameConstants.WIDTH/2
        if self.xPosition == GameConstants.WIDTH * 1.5:
            self.xPosition = -(GameConstants.WIDTH/2)
                        
            
class Fireball:
    def __init__ (self, character):
        self.position = Vector(character.position.x, character.position.y -20)
        self.movementSpeed = Vector(7,0)
        self.isActive = False
        self.character = character
        self.originalX = 165
        self.originalY = 55
        self.boss = character.footSoldierRight # used to help mage boss shoot fireball, takes place of footsoldier right

    def update(self):
        if(self.isActive):
            if(self.position.x > 800 + 55 or self.position.x < 0 - 55):
                self.isActive = False
            self.position.add(self.movementSpeed)
        else:
            if self.character.isMage == False:
                self.position = Vector(self.boss.position.x, self.boss.position.y - 40)
            else:
                self.position = Vector(character.position.x, character.position.y - 20)

    def draw(self, canvas):
        if(self.isActive):
            canvas.draw_image(GameConstants.FIRE_BALL_SPRITE_SHEET, (self.originalX, self.originalY), (110,110), (self.position.x, self.position.y), (55,55))

    def setActive(self):
        if(self.isActive == False):
            if self.character.isMage == False: # when true, means boss is the mage
                self.position = Vector(self.boss.position.x, self.boss.position.y - 30)
            else:
                self.position = Vector(self.character.position.x, self.character.position.y -30)
            self.isActive = True

class Keyboard:
    def __init__ (self):
        self.right = False
        self.rightDown = False
        self.left = False
        self.leftDown = False
        self.r = False # heavy attack
        self.f = False # light attack

    def keyDown(self, key):
        if self.rightDown == False:
             if key == simplegui.KEY_MAP['right'] or key == simplegui.KEY_MAP['d']:
                self.right = True
                self.rightDown = True
        
        if self.leftDown == False: 
            if key == simplegui.KEY_MAP['left'] or key == simplegui.KEY_MAP['a']:
                self.left = True
                self.leftDown = True
            
        if self.f == False: 
            if key == simplegui.KEY_MAP['r']: # heavyAttack
                self.r = True
            
        if self.r == False:
            if key == simplegui.KEY_MAP['f']: # lightAttack
                self.f = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right'] or key == simplegui.KEY_MAP['d']:
            self.right = False
            self.rightDown = False
        if key == simplegui.KEY_MAP['left'] or key == simplegui.KEY_MAP['a']:
            self.left = False
            self.leftDown = False

class Interaction:#contains all movements and collision handling/combat
    def __init__ (self, character, keyboard, endOfAttackRow):
        self.keyboard = keyboard
        self.MLA = GameConstants.MAGE_LIGHTATK
        self.MHA = GameConstants.MAGE_HEAVYATK
        self.SLA = GameConstants.SAMURAI_LIGHTATK
        self.SHA = GameConstants.SAMURAI_HEAVYATK
        self.character = character
        self.originalX = GameConstants.IMG_DIMS * 0.5
        self.originalY = GameConstants.IMG_DIMS * 0.5
        self.facingLeft = False
        self.facingRight = True
        self.leftIterator = 0
        self.rightIterator = 0
        self.lightAttackIterator = 0
        self.heavyAttackIterator = 0
        self.idleDetector = 120
        self.idleIterator = 0
        self.endOfAttackRow = endOfAttackRow
        self.fireballCooldown = 0
       
        self.fsrOriginalX = GameConstants.IMG_DIMS * 0.5
        self.fsrOriginalY = GameConstants.IMG_DIMS * 4.5
        self.fsrLeftIterator = 0
        self.fsrLightAttackIterator = 0
        self.fsrHeavyAttackIterator = 0
        self.fsrEndOfAttackRow = endOfAttackRow
        self.fsrGracePeriod = 0
        self.fsrRandomNumber = random.randint(0,1)
        self.fsrDamageTaken = 0
        
        self.fslOriginalX = GameConstants.IMG_DIMS * 0.5
        self.fslOriginalY = GameConstants.IMG_DIMS * 0.5
        self.fslRightIterator = 0
        self.fslLightAttackIterator = 0
        self.fslHeavyAttackIterator = 0
        self.fslEndOfAttackRow = endOfAttackRow
        self.fslGracePeriod = 0
        self.fslRandomNumber = random.randint(0,1)
        self.fslDamageTaken = 0
        
        self.volume = 1
        self.volume1 = 0
        self.i = 0
        
        self.damageTaken = 0
        self.regenIterator = 0
        
        self.miniBossTimer = 0
        self.bossTimer = 0
        self.isMiniBoss = False
        self.isBoss = False
        self.bossAttackPeriod = 0

    def idle(self):
        if self.facingRight:
            self.originalY = GameConstants.IMG_DIMS * 0.5
        else:
            self.originalY = GameConstants.IMG_DIMS * 4.5
        self.idleIterator += 1
        if self.originalX == GameConstants.IMG_DIMS * 3.5:
            self.originalX = GameConstants.IMG_DIMS * 0.5
        elif self.idleIterator == 20:
            self.originalX += GameConstants.IMG_DIMS
            self.idleIterator = 0
            

    def moveLeft(self):
        self.facingLeft = True
        self.facingRight = False
        self.originalY = GameConstants.IMG_DIMS * 5.5
        self.leftIterator += 1
        if self.originalX == (GameConstants.IMG_DIMS * 3.5) and self.leftIterator == 10: # after 4th frame, reset.
            self.originalX = GameConstants.IMG_DIMS * 0.5
            self.leftIterator = 0
        elif self.leftIterator == 10:
            self.originalX += GameConstants.IMG_DIMS
            self.leftIterator = 0

    def moveRight(self):
        self.facingRight = True
        self.facingLeft = False
        self.originalY = GameConstants.IMG_DIMS * 1.5
        self.rightIterator += 1
        if self.originalX == (GameConstants.IMG_DIMS * 3.5) and self.rightIterator == 10: # after 4th frame, reset.
            self.originalX = GameConstants.IMG_DIMS * 0.5
            self.rightIterator = 0
        elif self.rightIterator == 10:
            self.originalX += GameConstants.IMG_DIMS
            self.rightIterator = 0

    def lightAttack(self):
        if self.character.isMage :
           self.MLA.play()
        if self.character.isMage == False:
           self.SLA.play()
            
            
        self.keyboard.left = False # Stops movement of sprite during attack
        self.keyboard.right = False # Stops movement of sprite during attack
        if self.facingRight: # if facing right
            self.originalY = GameConstants.IMG_DIMS * 3.5 # use right attack
        if self.facingLeft: # if facing left
            self.originalY = GameConstants.IMG_DIMS * 7.5 # use left attack
        self.lightAttackIterator += 1 # iterator variable updates to move across sprite sheet
        if self.originalX == self.endOfAttackRow and self.lightAttackIterator == 4: # if end of a row
            if self.character.inContactRight and self.facingRight:
                self.fsrDamageTaken += 0.5
            if self.character.inContactLeft and self.facingLeft:
                self.fslDamageTaken += 0.5
            if self.facingLeft:
                self.originalY = GameConstants.IMG_DIMS * 5.5 # returns it to left idle animation
                if self.keyboard.leftDown:
                    self.keyboard.left = True
            elif self.facingRight:
                self.originalY = GameConstants.IMG_DIMS * 1.5
                if self.keyboard.rightDown:
                    self.keyboard.right = True
            self.originalX = GameConstants.IMG_DIMS * 0.5
            self.keyboard.f = False
            self.lightAttackIterator = 0
        elif self.lightAttackIterator == 4:
            self.originalX += GameConstants.IMG_DIMS
            self.lightAttackIterator = 0
  
    def heavyAttack(self):
        if self.character.isMage :
           self.MHA.play()
        if self.character.isMage == False:
            self.SHA.play()
        
        self.keyboard.left = False
        self.keyboard.right = False
        if self.facingRight:
            self.originalY = GameConstants.IMG_DIMS * 2.5
        if self.facingLeft:
            self.originalY = GameConstants.IMG_DIMS * 6.5
        self.heavyAttackIterator += 1
        if self.originalX == self.endOfAttackRow and self.heavyAttackIterator == 6: # after 4th frame, reset.
            if self.character.inContactRight and self.facingRight:
                if self.character.isMage == False:
                    self.fsrDamageTaken += 1
            if self.character.inContactLeft and self.facingLeft:
                if self.character.isMage == False:
                    self.fslDamageTaken += 1
            if self.facingLeft:
                if self.keyboard.leftDown:
                    self.keyboard.left = True
                self.originalY = GameConstants.IMG_DIMS * 5.5 # returns it to last walking animation
            elif self.facingRight:
                self.originalY = GameConstants.IMG_DIMS * 1.5
                if self.keyboard.rightDown:
                    self.keyboard.right = True
            self.originalX = GameConstants.IMG_DIMS * 0.5
            self.keyboard.r = False
            self.heavyAttackIterator = 0
        elif self.heavyAttackIterator == 6:
            self.originalX += GameConstants.IMG_DIMS
            self.heavyAttackIterator = 0
        
    def fsrMoveLeft(self):
        self.fsrOriginalY = GameConstants.IMG_DIMS * 5.5
        if self.isBoss and self.character.isMage == False:
            self.character.footSoldierRight.vel.add(Vector(-0.2, 0))
        else:
            self.character.footSoldierRight.vel.add(Vector(-0.4, 0))
        self.fsrLeftIterator += 1
        if self.fsrOriginalX == (GameConstants.IMG_DIMS * 3.5) and self.fsrLeftIterator == 10: # after 4th frame, reset.
            self.fsrOriginalX = GameConstants.IMG_DIMS * 0.5
            self.fsrLeftIterator = 0
        elif self.fsrLeftIterator == 10:
            self.fsrOriginalX += GameConstants.IMG_DIMS
            self.fsrLeftIterator = 0
            
    def fsrLightAttack(self):
        self.fsrGracePeriod += 1
        if self.fsrGracePeriod >= 60 or self.isBoss:
            self.fsrOriginalY = GameConstants.IMG_DIMS * 7.5 # use left attack
            self.fsrLightAttackIterator += 1 # iterator variable updates to move across sprite sheet
            if self.fsrOriginalX == self.fsrEndOfAttackRow and self.fsrLightAttackIterator == 4: # if end of a row
                self.bossAttackPeriod = 0
                if self.character.inContactRight and self.isBoss:
                    self.damageTaken += 0.5
                elif self.character.inContactRight and self.isMiniBoss:
                    self.damageTaken += 1
                elif self.character.inContactRight:
                    self.damageTaken += 0.5
                self.fsrOriginalY = GameConstants.IMG_DIMS * 5.5 # returns it to left idle animation
                self.fsrOriginalX = GameConstants.IMG_DIMS * 0.5
                self.fsrLightAttackIterator = 0
                self.fsrGracePeriod = 0
                self.fsrRandomNumber = random.randint(0,1)
            elif self.fsrLightAttackIterator == 4:
                self.fsrEndOfAttack = True
                self.fsrOriginalX += GameConstants.IMG_DIMS
                self.fsrLightAttackIterator = 0
                
    def fsrHeavyAttack(self):
        self.fsrGracePeriod += 1
        if self.fsrGracePeriod >= 60 or self.isBoss:
            if self.character.isMage == False and self.isBoss: # If mage boss, launch fireball
                self.character.fireball.movementSpeed = Vector(-7,0)
                self.character.fireball.originalY = 165
                self.character.fireball.setActive()
            self.fsrOriginalY = GameConstants.IMG_DIMS * 6.5
            self.fsrHeavyAttackIterator += 1
            if self.fsrOriginalX == self.fsrEndOfAttackRow and self.fsrHeavyAttackIterator == 6: # after 4th frame, reset.
                self.bossAttackPeriod = 0
                if self.character.inContactRight and self.isMiniBoss:
                    self.damageTaken += 1.5
                elif self.character.inContactRight:
                    self.damageTaken += 1
                self.fsrOriginalY = GameConstants.IMG_DIMS * 5.5 # returns to walking animation
                self.fsrOriginalX = GameConstants.IMG_DIMS * 0.5
                self.fsrHeavyAttackIterator = 0
                self.fsrGracePeriod = 0
                self.fsrRandomNumber = random.randint(0,1)
            elif self.fsrHeavyAttackIterator == 6:
                self.fsrOriginalX += GameConstants.IMG_DIMS
                self.fsrHeavyAttackIterator = 0      
                
    def fslMoveRight(self):
        self.fslFacingLeft = False
        self.fslFacingRight = True
        self.fslOriginalY = GameConstants.IMG_DIMS * 1.5
        self.character.footSoldierLeft.vel.add(Vector(0.4, 0))
        self.fslRightIterator += 1
        if self.fslOriginalX == (GameConstants.IMG_DIMS * 3.5) and self.fslRightIterator == 10: # after 4th frame, reset.
            self.fslOriginalX = GameConstants.IMG_DIMS * 0.5
            self.fslRightIterator = 0
        elif self.fslRightIterator == 10:
            self.fslOriginalX += GameConstants.IMG_DIMS
            self.fslRightIterator = 0
            
    def fslLightAttack(self):
        self.fslGracePeriod += 1
        if self.fslGracePeriod >= 60:
            self.fslOriginalY = GameConstants.IMG_DIMS * 3.5 # use left attack
            self.fslLightAttackIterator += 1 # iterator variable updates to move across sprite sheet
            if self.fslOriginalX == self.fslEndOfAttackRow and self.fslLightAttackIterator == 4: # if end of a row
                if self.character.inContactLeft:
                    self.damageTaken += 0.5
                self.fslOriginalY = GameConstants.IMG_DIMS * 1.5 # returns it to left idle animation
                self.fslOriginalX = GameConstants.IMG_DIMS * 0.5
                self.fslLightAttackIterator = 0
                self.fslGracePeriod = 0
                self.fslRandomNumber = random.randint(0,1)
            elif self.fslLightAttackIterator == 4:
                self.fslEndOfAttack = True
                self.fslOriginalX += GameConstants.IMG_DIMS
                self.fslLightAttackIterator = 0
                
    def fslHeavyAttack(self):
        self.fslGracePeriod += 1
        if self.fslGracePeriod >= 60:
            self.fslOriginalY = GameConstants.IMG_DIMS * 2.5
            self.fslHeavyAttackIterator += 1
            if self.fslOriginalX == self.fslEndOfAttackRow and self.fslHeavyAttackIterator == 6: # after 4th frame, reset.
                if self.character.inContactLeft:
                    self.damageTaken += 1
                self.fslOriginalY = GameConstants.IMG_DIMS * 1.5 # returns to walking animation
                self.fslOriginalX = GameConstants.IMG_DIMS * 0.5
                self.fslHeavyAttackIterator = 0
                self.fslGracePeriod = 0
                self.fslRandomNumber = random.randint(0,1)
            elif self.fslHeavyAttackIterator == 6:
                self.fslOriginalX += GameConstants.IMG_DIMS
                self.fslHeavyAttackIterator = 0

    def update(self):
        GameConstants.GENERAL_MUSIC.set_volume(0.3) # done to allow SFX to be heard over the audio
        
        if self.keyboard.left and self.keyboard.leftDown:
            # make characters turn around regardless of whether there is something in contact
            self.originalY = 4.5 * GameConstants.IMG_DIMS
            self.facingLeft = True
            self.facingRight = False
            if self.character.inContactLeft == False:
                self.idleDetector = 0
                self.rightIterator = 0
                self.lightAttackIterator
                self.heavyAttackIterator = 0
                Interaction.moveLeft(self)

        if self.keyboard.right and self.keyboard.rightDown:
            self.originalY = 0.5 * GameConstants.IMG_DIMS
            self.facingRight = True
            self.facingLeft = False
            if self.character.inContactRight == False:
                self.idleDetector = 0     
                self.leftIterator = 0
                self.lightAttackIterator
                self.heavyAttackIterator = 0
                Interaction.moveRight(self)

        if self.keyboard.f:
            self.idleDetector = 0
            self.leftIterator = 0
            self.rightIterator = 0
            self.heavyAttackIterator = 0
            Interaction.lightAttack(self)

        #------------------------------------ Performs the R attack based on keyboard input
        
        if self.keyboard.r:
            self.idleDetector = 0
            self.leftIterator = 0
            self.rightIterator = 0
            self.lightAttackIterator = 0
            
            #------------------------------------ If mage, shoot fireball in direction mage is facing
            
            if self.character.isMage:
                if self.fireballCooldown <= 0 or self.character.fireball.isActive:
                    if self.damageTaken < 3:
                        self.fireballCooldown = 60
                        self.character.IMG = GameConstants.MAGE_SPRITE_SHEET
                        
                    if self.facingLeft:
                        self.character.fireball.movementSpeed = Vector(-7,0)
                        self.character.fireball.originalY = 165 # Changes the frame of the spritesheet based on direction of travel
                    else:
                        self.character.fireball.movementSpeed = Vector(7,0)
                        self.character.fireball.originalY = 55 # Changes the frame of the spritesheet based on direction of travel
                    if self.character.fireball.isActive == False:
                        self.character.fireball.setActive()
            Interaction.heavyAttack(self)
                                
        if self.keyboard.left == False and self.keyboard.right == False and self.keyboard.f == False and self.keyboard.r == False:
            self.originalY = 4.5 * GameConstants.IMG_DIMS
            if self.facingRight:
                self.originalY = 0.5 * GameConstants.IMG_DIMS

        self.idleDetector += 1
        if self.idleDetector > 120: # if left untouched for 2 seconds, idle animation starts until other animation starts
            Interaction.idle(self)
        
        
        if self.damageTaken >= 3 and self.character.isMage: # if half heath, go to red mode, cooldown decreased
            self.character.IMG = GameConstants.MAGE_RED_SPRITE_SHEET
            self.fireballCooldown = 0
        #------------------------------------ Checking for right footsoldier collisions
        
        if self.character.footSoldierRight.position.x - self.character.footSoldierRight.hitbox > self.character.position.x + self.character.hitbox:
            self.character.inContactRight = False

        if self.character.footSoldierRight.position.x - self.character.footSoldierRight.hitbox <= self.character.position.x + self.character.hitbox:
            self.character.inContactRight = True
        
        #------------------------------------- Checking for fireball collisions with right footsoldier / enemy
        
        if self.character.isMage: # If character is mage, boss is not mage, this determines the function of the fireball 
            if (self.character.fireball.position.x - 55 > self.character.footSoldierRight.position.x - self.character.footSoldierRight.hitbox):
                self.character.fireball.isActive = False
                self.fsrDamageTaken += 1 # damage of mage fireball
        else:
            if self.character.fireball.isActive:
                if (self.character.fireball.position.x - 55 < self.character.position.x + self.character.hitbox):
                    self.character.fireball.isActive = False
                    if self.keyboard.r == False:
                        self.damageTaken += 2 # Damage that mage boss deals upon impact of fireball
            
        #-------------------------------------- Respawning foot soldiers   
        
        if self.isMiniBoss == False and self.isBoss == False and self.fsrDamageTaken >= 2.5: # health of footsoldier right
            self.fsrOriginalX = GameConstants.IMG_DIMS * 0.5
            self.fsrOriginalY = GameConstants.IMG_DIMS * 4.5
            self.character.footSoldierRight.position.x = GameConstants.WIDTH + random.randint(self.character.footSoldierRight.hitbox, self.character.footSoldierRight.hitbox * 10)
            self.fsrDamageTaken = 0
            self.character.score += 100
            
        if self.isMiniBoss and self.fsrDamageTaken >= 7.5: # dictates health of mini boss
            self.isMiniBoss = False
            self.fsrOriginalX = GameConstants.IMG_DIMS * 0.5
            self.fsrOriginalY = GameConstants.IMG_DIMS * 4.5
            self.character.footSoldierRightImage = GameConstants.FOOT_SOLDIER_SPRITE_SHEET
            self.character.footSoldierRight_img_dest_dim = 128, 128
            self.character.footSoldierRight_hitbox = 64
            self.character.footSoldierRight.position.x = GameConstants.WIDTH + random.randint(self.character.footSoldierRight.hitbox, self.character.footSoldierRight.hitbox * 10)
            self.fsrDamageTaken = 0
            self.character.score += 1000
                    
        if self.character.inContactRight == False and self.isBoss:
                self.bossAttackPeriod += 1
                if (self.bossAttackPeriod >= 30 and self.character.isMage == False):
                    Interaction.fsrHeavyAttack(self)
                    
                elif self.bossAttackPeriod >= 30 and self.character.isMage: # If samurai boss, attack whilst not in contact every 1.5s, gives mage time to shoot him down
                    Interaction.fsrHeavyAttack(self)
                    
                    # boss attack period resets in heavy attack if attack is complete
                else:
                    Interaction.fsrMoveLeft(self)
            
        elif self.character.inContactRight == False:
                Interaction.fsrMoveLeft(self)
            
        elif self.character.inContactRight: #--------- if in contact with mage boss, light attack (fireballs close range would be too OP)
            if self.isBoss and self.character.isMage == False:
                Interaction.fsrLightAttack(self)
                
            elif self.fsrRandomNumber == 0: #------------ if not mage boss, randomly use light attack or heavy attack when in contact
                Interaction.fsrLightAttack(self)
            else:
                Interaction.fsrHeavyAttack(self)

        # until footsoldier reaches character, move towards character
        
        if self.character.footSoldierLeft.position.x + self.character.footSoldierLeft.hitbox < self.character.position.x - self.character.hitbox:
            self.character.inContactLeft = False

        if self.character.footSoldierLeft.position.x + self.character.footSoldierLeft.hitbox >= self.character.position.x - self.character.hitbox:
            self.character.inContactLeft = True	

        if (self.character.fireball.position.x + 55 < self.character.footSoldierLeft.position.x + self.character.footSoldierLeft.hitbox):
            self.character.fireball.isActive = False
            self.fslDamageTaken += 1 # damage of player mage fireball
            
        if (self.fslDamageTaken >= 2.5): # foot soldier left health
            self.fslOriginalX = GameConstants.IMG_DIMS * 0.5
            self.fslOriginalY = GameConstants.IMG_DIMS * 0.5
            self.character.footSoldierLeft.position.x = 0 - random.randint(self.character.footSoldierLeft.hitbox, self.character.footSoldierLeft.hitbox * 10)
            self.fslDamageTaken = 0
            self.character.score += 100
        
        #---------------------- Removes left footsoldier from screen when bosses show up
        
        if self.isMiniBoss == False and self.isBoss == False:
            if self.character.inContactLeft == False:
                Interaction.fslMoveRight(self) # moves right until reaches character
            
            #------------------------ Once in contact, randomly use light or heavy attack
            
            elif self.character.inContactLeft:
                if self.fslRandomNumber == 0:
                    Interaction.fslLightAttack(self)
                else:
                    Interaction.fslHeavyAttack(self)
        else:
            self.character.footSoldierLeft.position.x = 0 - random.randint(self.character.footSoldierRight.hitbox, self.character.footSoldierRight.hitbox * 10) # adds a random element to spawn, other score will add up the same and will be repetitive
        
        if self.regenIterator == 90 and self.damageTaken > 0 and self.character.isMage:
            self.damageTaken -= 0.5
        elif self.regenIterator == 120 and self.damageTaken > 0 and self.character.isMage == False:
            self.damageTaken -= 0.5
        if self.regenIterator == 120:
            self.regenIterator = 0
            
        #----------------- Calculating the variation of hearts to display
        
        if self.character.isMage == False:
            if self.damageTaken >= 0.5 and self.damageTaken > 0:
                self.character.hearts[9] = GameConstants.HALF_HEART_IMAGE
            if self.damageTaken >= 1:
                self.character.hearts[9] = GameConstants.EMPTY_HEART_IMAGE
            if self.damageTaken >= 1.5:
                self.character.hearts[8] = GameConstants.HALF_HEART_IMAGE
            if self.damageTaken >= 2:
                self.character.hearts[8] = GameConstants.EMPTY_HEART_IMAGE
            if self.damageTaken >= 2.5:
                self.character.hearts[7] = GameConstants.HALF_HEART_IMAGE
            if self.damageTaken >= 3:
                self.character.hearts[7] = GameConstants.EMPTY_HEART_IMAGE
            if self.damageTaken >= 3.5:
                self.character.hearts[6] = GameConstants.HALF_HEART_IMAGE
            if self.damageTaken >= 4:
                self.character.hearts[6] = GameConstants.EMPTY_HEART_IMAGE
            if self.damageTaken >= 4.5:
                self.character.hearts[5] = GameConstants.HALF_HEART_IMAGE

        if self.damageTaken >= 0.5 and self.character.isMage and self.damageTaken > 0:
            self.character.hearts[5] = GameConstants.HALF_HEART_IMAGE
        if self.damageTaken >= 5 or (self.damageTaken >= 1 and self.character.isMage):
            self.character.hearts[5] = GameConstants.EMPTY_HEART_IMAGE
        if self.damageTaken >= 5.5 or (self.damageTaken >= 1.5 and self.character.isMage):
            self.character.hearts[4] = GameConstants.HALF_HEART_IMAGE
        if self.damageTaken >= 6 or (self.damageTaken >= 2 and self.character.isMage):
            self.character.hearts[4] = GameConstants.EMPTY_HEART_IMAGE
        if self.damageTaken >= 6.5 or (self.damageTaken >= 2.5 and self.character.isMage):
            self.character.hearts[3] = GameConstants.HALF_HEART_IMAGE
        if self.damageTaken >= 7 or (self.damageTaken >= 3 and self.character.isMage):
            self.character.hearts[3] = GameConstants.EMPTY_HEART_IMAGE
        if self.damageTaken >= 7.5 or (self.damageTaken >= 3.5 and self.character.isMage):
            self.character.hearts[2] = GameConstants.HALF_HEART_IMAGE
        if self.damageTaken >= 8 or (self.damageTaken >= 4 and self.character.isMage):
            self.character.hearts[2] = GameConstants.EMPTY_HEART_IMAGE
        if self.damageTaken >= 8.5 or (self.damageTaken >= 4.5 and self.character.isMage):
            self.character.hearts[1] = GameConstants.HALF_HEART_IMAGE
        if self.damageTaken >= 9 or (self.damageTaken >= 5 and self.character.isMage):
            self.character.hearts[1] = GameConstants.EMPTY_HEART_IMAGE
        if self.damageTaken >= 9.5 or (self.damageTaken >= 5.5 and self.character.isMage):
            self.character.hearts[0] = GameConstants.HALF_HEART_IMAGE

        if self.damageTaken >= 10 or (self.damageTaken >= 6 and self.character.isMage):
            self.character.heart1 = GameConstants.EMPTY_HEART_IMAGE
            # this if statement, when true, means the game over SCREEN should be displayed            
            GameConstants.GAME_STATE = 0
            GameConstants.GAMEOVERSFX.play()

        self.character.img_centre = (self.originalX, self.originalY)
        self.character.footSoldierRight.img_centre = (self.fsrOriginalX, self.fsrOriginalY)
        self.character.footSoldierLeft.img_centre = (self.fslOriginalX, self.fslOriginalY)
        
        if self.miniBossTimer == 3600: # after 1 minute 3600, spawn mini boss
            self.character.backgroundImage = GameConstants.BACKGROUND_AFTERNOON_IMAGE
            self.isMiniBoss = True
            self.character.footSoldierRightImage = GameConstants.FOOT_SOLDIER_BLUE_SPRITE_SHEET
            self.character.footSoldierRight_img_dest_dim = 128 * 1.5, 128 * 1.5
            self.character.footSoldierRight_hitbox = 64 * 1.5
            self.character.footSoldierRight.position.x = GameConstants.WIDTH + self.character.footSoldierRight.hitbox
            
        if self.bossTimer == 7200: # after 2 minutes 7200, spawn boss
            self.damageTaken = 0
            self.character.backgroundImage = GameConstants.BACKGROUND_NIGHT_IMAGE
            self.isBoss = True
            self.character.footSoldierRightImage = GameConstants.MAGE_SPRITE_SHEET
            self.character.footSoldierRight_img_dest_dim = 128 * 1.5, 128 * 1.5
            self.character.footSoldierRight_hitbox = 64 * 1.5
            self.character.footSoldierRight.position.x = GameConstants.WIDTH + self.character.footSoldierRight.hitbox # We want the boss to arrive as soon as the background switches
            
            if self.character.isMage:
                self.character.footSoldierRightImage = GameConstants.SAMURAI_SPRITE_SHEET
            
        self.regenIterator += 1
        self.fireballCooldown -= 1

        if self.miniBossTimer < 3601:
            self.miniBossTimer += 1
            
        if self.bossTimer < 7201:
            self.bossTimer += 1 # final number left over 7200 to not trigger if statement again, but stops timer to ease pressure on the programme
            
        if self.isBoss and self.fsrDamageTaken >= 10.5: # game winning condition, boss health
            self.character.score += 5000
            GameConstants.VICTORYSFX.play()
            GameConstants.GAME_STATE = 3
    
def event_handler(pos):
        if GameConstants.SCREEN == 0:    
            if pos[0] >= 246 and pos [0] <= 500:
                if pos [1] >= 194 and pos[1] <= 250: start.set_button()
                
        elif GameConstants.SCREEN == 1:
            if pos[0] >= 240 and pos[0] <= 350:
                if pos [1] >= 150 and pos[1] <= 340: 
                    GameConstants.CHAR_SELECTED = "Samurai"
                    start.show_storyboard()
                    
            if pos[0] >= 430 and pos [0] <= 560:
                if pos [1] >= 150 and pos[1] <= 340: 
                    GameConstants.CHAR_SELECTED = "Mage"
                    start.show_storyboard()
            
        elif GameConstants.SCREEN == 2: 
            if pos[0] >= 625 and pos[0] <= 780:
                if pos[1] >= 375 and pos[1] <= 430: 
                    GameConstants.GAME_STATE = 2
        
        #-------------------------------------------------------------------------------------
        
        # HERE ADDED ONE MORE CONDITION TO HANDLE THE CLICK OF `PLAY AGAIN` BUTTON FROM 
        
        # GAME OVER SCREEN
        
        #-------------------------------------------------------------------------------------
        if GameConstants.GAME_STATE == 0 or GameConstants.GAME_STATE == 3:   
            GameConstants.WELCOME_SCREEN_MUSIC.play()
            if pos[0] >= 246 and pos [0] <= 500:
                if pos [1] >= 194 and pos[1] <= 250: 
                    start.game_reset()
                    GameConstants.GAME_STATE = 1
                    
                    
kbd = Keyboard()
character = None
inter = None
start = StartGame()
end = EndGame()
victory = None

def draw(canvas):
    global character
    global inter
    global victory
    
    #-----------------------------------------------------------------------------------------
    
    # HERE ALSO, CHANGED THE CONDITION WITH `gameState` VARIABLE, REMOVING THE RELIANCE ON 
    
    # ONE STATE VARIABLES i.e, `gameOver` and `gameStarted`
    
    #-----------------------------------------------------------------------------------------
    
    if GameConstants.GAME_STATE == 0:
        end.draw(canvas)  
        GameConstants.WELCOME_SCREEN_MUSIC.rewind()
        GameConstants.GENERAL_MUSIC.rewind()
        GameConstants.SCREEN = 0
        
    elif GameConstants.GAME_STATE == 1:
        GameConstants.WELCOME_SCREEN_MUSIC.play()
        start.draw(canvas)
        footSoldierRight = FootSoldier(GameConstants.FOOT_SOLDIER_SPRITE_SHEET, True)
        footSoldierLeft = FootSoldier(GameConstants.FOOT_SOLDIER_SPRITE_SHEET, False)
        
          
        if GameConstants.CHAR_SELECTED == "Samurai":
            character = Player(GameConstants.SAMURAI_SPRITE_SHEET, footSoldierRight, footSoldierLeft, kbd, False)
            victory = Victory(character)
            inter = Interaction(character, kbd, GameConstants.IMG_DIMS * 4.5)
        
        elif GameConstants.CHAR_SELECTED == "Mage":
            character = Player(GameConstants.MAGE_SPRITE_SHEET, footSoldierRight, footSoldierLeft, kbd, True)
            victory = Victory(character)
            inter = Interaction(character, kbd, GameConstants.IMG_DIMS * 3.5)

    elif GameConstants.GAME_STATE == 2:
        character.update()
        GameConstants.WELCOME_SCREEN_MUSIC.rewind()
        GameConstants.GENERAL_MUSIC.play()
        character.background.update(canvas)
        character.footSoldierRight.update()
        character.footSoldierLeft.update()
        character.draw(canvas)
        character.fireball.update()
        character.fireball.draw(canvas)
        inter.update()

    if GameConstants.GAME_STATE == 3:
        GameConstants.WELCOME_SCREEN_MUSIC.rewind()
        victory.draw(canvas)
        GameConstants.SCREEN = 0

frame = simplegui.create_frame('Heroes Rising', GameConstants.WIDTH, GameConstants.HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.set_mouseclick_handler(event_handler)
frame.start()