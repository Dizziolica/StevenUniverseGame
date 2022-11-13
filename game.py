
import multiprocessing
import pygame
from sys import exit
from random import randint
from moviepy.editor import *
from pygame import mixer
from playsound import playsound
import multiprocessing
from threading import Thread
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
from multiprocessing import Process
from pydub.playback import _play_with_simpleaudio
import vlc 
import time


        


black = (0, 0, 0)
white = (255, 255, 255)
x = 80
y = 390
score = 0
start_time = 0
color = (255,0,255)
counter = 0

test_font = pygame.font.SysFont('Pixe.ttf', 50)
screen = pygame.display.set_mode((800, 600))
sky_surface = pygame.image.load('background.png').convert()
default_sky_size = (800,400)
sky_image = pygame.transform.scale(sky_surface, default_sky_size)


ground_surface = pygame.image.load('ground.png').convert_alpha()
default_ground_size = (800,100)
ground_image = pygame.transform.scale(ground_surface, default_ground_size)


Peri_surface = pygame.image.load('Peri.png').convert_alpha()
default_Peri_size = (200,200)
Peri_image = pygame.transform.scale(Peri_surface, default_Peri_size)
Peri_rect = Peri_image.get_rect( midleft = (600, 325))

green_surface = pygame.image.load('green.png').convert_alpha()
default_green_size = (50,50)
green_image = pygame.transform.scale(green_surface, default_green_size)
green_rect = green_image.get_rect(midleft = (400, 300))
green_timer = pygame.USEREVENT + 1
pygame.time.set_timer(green_timer, 2500)
green_rect_list = []

       

biscoito_surface = pygame.image.load('biscoito.png').convert_alpha()
default_biscoito_size = (50,50)
biscoito_image = pygame.transform.scale(biscoito_surface, default_biscoito_size)
biscoito_rect = biscoito_image.get_rect(midleft = (600, 350))


pink_surface = pygame.image.load('ballpink.png').convert_alpha()
pink_green_size = (150,120)
pink_image = pygame.transform.scale(pink_surface, pink_green_size)
pink_rect = pink_image.get_rect(midbottom = (x, y))

steven_surface = pygame.image.load('steven.png').convert_alpha()
steven_surface2 = pygame.image.load('steven.png').convert_alpha()
default_steven_size = (100, 100)
steven_image = pygame.transform.scale(steven_surface, default_steven_size)
steven_image2 = pygame.transform.scale(steven_surface2, default_steven_size)
steven_gravity = 0
steven_index = 0

steven_rect = steven_image.get_rect(midbottom = (x, y))
steven_rect2 = steven_image2.get_rect(midbottom = (x, y))
steven_walk = [steven_image, steven_image2]
steven_index = 0
steven_jump = pygame.image.load('steven.png').convert_alpha()


Ametista_surface = pygame.image.load('Ametista.png').convert_alpha()
default_Ametista_size = (150,150)
Ametista_image = pygame.transform.scale(Ametista_surface, default_Ametista_size)
Ametista_rect = Ametista_image.get_rect( midleft = (296, 400))

perola_surface = pygame.image.load('perola.png').convert_alpha()
default_perola_size = (100,100)
perola_image = pygame.transform.scale(perola_surface, default_perola_size)
perola_rect = perola_image.get_rect( midleft = (100, -5))

fala_surface = pygame.image.load('fala.png').convert_alpha()
default_fala_size = (200,200)
fala_image = pygame.transform.scale(fala_surface, default_fala_size)
fala_rect = fala_image.get_rect( midleft = (220, 380))

Garnet_surface = pygame.image.load('garnet.png').convert_alpha()
default_Garnet_size = (150,150)
Garnet_image = pygame.transform.scale(Garnet_surface, default_Garnet_size)
Garnet_timer = pygame.USEREVENT + 1
Garnet_rect = Ametista_image.get_rect( midleft = (608, 38))
pygame.time.set_timer(Garnet_timer, 8000)


game_name = test_font.render('Pixel Runner',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to run',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,330))

current_time = int(pygame.time.get_ticks() / 1000 ) - start_time
score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
score_message_rect = score_message.get_rect(center = (400,330))



class Steven(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        
        self.steven_walk = [steven_rect, steven_rect]
        
        
        self.surf = self.steven_walk[steven_index]
       
        self.rect = steven_image.get_rect(midbottom = (390, 80))
        
        steven_gravity = 0
    
        
    def steven_move(self):

    
        keys = pygame.key.get_pressed()
       

                    
        if keys[pygame.K_RIGHT]:
            steven_rect.x += 10

        if keys[pygame.K_LEFT]:
            steven_rect.x -= 10
        

    def apply_gravity():

        steven_gravity = +1
        steven_rect.y += steven_gravity
        if steven_rect.bottom >= 390:
            steven_rect.bottom = 390
        if steven_rect.right <= - 100 or steven_rect.left >= 800:
            steven_rect.right = 80

    def animation_state(self):

        if steven_rect.bottom < 390:
            steven_image = steven_rect
         
        else:

            steven_index = +0.1
            if steven_index > len(self.steven_walk):
            
                steven_image = self.steven_walk[int(steven_index)]
    
    
        

    
        
       
            
        
            
            
             
           
            
            
            
            


    def updateSteven(self):

        self.steven_move()    
        self.apply_gravity()
        self.animation_state()
        



class Pink(pygame.sprite.Sprite):

    def __init__(self):
        
        super().__init__()
    
        pink_surface = pygame.image.load('ballpink.png').convert_alpha()
        pink_green_size = (150,120)
        pink_image = pygame.transform.scale(pink_surface, pink_green_size)
        pink1 = pygame.transform.scale(pink_surface, pink_green_size)
        pink2 = pygame.transform.scale(pink_surface, pink_green_size)
        frames =[pink1, pink2]
        y_pos = 0
        pink_gravity = 0
        self.animation_index = 0
        self.image = frames[self.animation_index]
    
        

    def animation_state(self):

            self.animation_index += 0.1
            if self.animation_index >= len(self.frames):
                self.animation_index = 0
                self.image = self.frames[int(self.animation_index)]

    def movePink(self):

    
            if pink_rect.bottom >= 390:
                pink_rect.bottom = 390
                
    
            if pink_rect.right <= -100 or pink_rect.left >= 800:
                
                pink_rect.right = 80

    def pinkInput(self):
        
        

        keys = pygame.key.get_pressed()

        if keys[pygame.MOUSEBUTTONDOWN]:

            if steven_rect.collidepoint(event.pos) and steven_rect.bottom >= 300:
                print('collision')
                    
                pink_gravity = -25

        if keys[pygame.K_SPACE] and pink_rect.bottom >= 390:

            pink_gravity = -25
        
        
        
        
     
        if keys[pygame.K_RIGHT]:

            pink_rect.x += 20

        if keys[pygame.K_LEFT]:
            pink_rect.x -= 20

    def pinkGravity(self):

        pink_gravity += 1
        pink_rect.y += pink_gravity
        if pink_rect.bottom >= 390:
            pink_rect.bottom = 390
    
    def updatePink(self):

        self.animation_state()
        self.movePink()
        self.pinkInput()
        self.pinkGravity()





class Green(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        
        green_rect = green_image.get_rect(midleft = (400, 300))

    

    def moveGreen(self):

        
        

        green_rect.x -= 5
        if green_rect.right < - 100:
            green_rect.left = 600
        

    def collisionsGreen(self):

        
        

            
        if green_rect.colliderect(steven_rect):   
            '''screen.fill((200,200,200)) 
            capa = pygame.image.load('/home/dizziolica/Music/Steven/img/capa.jpeg').convert_alpha()
            capa_size = (800, 400)
            capa_image = pygame.transform.scale(capa, capa_size)
            capa_rect = capa_image.get_rect(center = (400, 200))
            screen.blit(capa_image, capa_rect)
            steve_surface = pygame.image.load('/home/dizziolica/Music/Steven/img/steven.png').convert_alpha()
            steve_size = (100, 100)
            steve_image = pygame.transform.scale(steve_surface, steve_size)
            steve_rect = steve_image.get_rect(midleft = (600, 400))
            screen.blit(steve_image, steve_rect)''' 

            lose = pygame.image.load('lose.png').convert_alpha()
            lose_size = (800,400)
            lose_image = pygame.transform.scale(lose, lose_size)
            lose_rect = lose_image.get_rect(center = (400,200))
            screen.blit(lose_image, lose_rect)
            
            
            
           

         
               
            
    
        
class catCookie(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        
        self.biscoito1 = pygame.transform.scale(biscoito_surface, default_biscoito_size)
        self.biscoito2 = pygame.transform.scale(biscoito_surface, default_biscoito_size)
        self.frames = [self.biscoito1, self.biscoito2]
        self.y_pos = 350
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]

    def display_score(self):

        
        score_surface = test_font.render(f'Score: {counter}', False, (64,64,64))
        score_image_size = (50, 50)
        score_image = pygame.transform.scale(score_surface, score_image_size)
        score_rect = score_image.get_rect(center = (410, 127))
        pygame.draw.rect(screen, color, score_rect)
        pygame.draw.rect(screen,color, score_rect, 10)
        screen.blit(score_image, score_rect)
        
        
    def animation_state(self):

        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
            self.image = self.frames[int(self.animation_index)]

    def moveCookie(biscoito_list):
        
        
        biscoito_rect.x -= 3
        if biscoito_rect.right < - 100 : 
        
            biscoito_rect.left = 800

        screen.blit(biscoito_image, biscoito_rect)

        
   
       

    def collision_sprite(self):

       
        
        
        if biscoito_rect.colliderect(steven_rect):
    
            screen.blit(pink_image, pink_rect)
            screen.blit(steven_image, steven_rect)
            screen.blit(Ametista_image, Ametista_rect)
            
            screen.blit(fala_image, fala_rect)
            screen.blit(Garnet_image, Garnet_rect)
            pygame.time.delay(50)
            green_rect.x = 600
            screen.blit(perola_image, perola_rect)
            
            
            

    def updateCookie(self):

        self.animation_state()  
        self.moveCookie()   
        self.collision_sprite()

    
        
       
		
        
            
            
   
        

    

def collision_sprite(self):

    if pygame.sprite.spritecollide(Steven1.sprite, Green, False):

        Green.empty
        return False

    else: 
        return True


def green_movement(green_list):

    if green_list:
            for green_rect in green_list:
                green_rect.x -=  5

                screen.blit(green_image, green_rect)

            return green_list

            
    else:
        return[]
    


    
  

            
  

           
  

            

    
   

        
pygame.mixer.init()
playsound("Abertura.mp3",False)

'''pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('Abertura.mp3')
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()
pygame.init()'''



'''pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=4096)
playsound('Abertura.mp3', False)'''




screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Steven Universe')
clock = pygame.time.Clock()






biscoito = catCookie()
biscoito.updateCookie()
biscoito.display_score()
width = 800
height = 400
velocity = 12
y = 390
x = 80
start_time = 0
color = (255,0,255)
score = 0
game_active = False








'''p = multiprocessing.Process(target=playsound, args=("Abertura.mp3", False))
p.start()
input("press ENTER to stop playback")
p.terminate()'''


steven = pygame.sprite.GroupSingle()
steven.add(Steven())

green = pygame.sprite.GroupSingle()
green.add(Green())







  









while True:

    
          
    for event in pygame.event.get():

       
           
        
           
        

        if event.type == pygame.QUIT:
            pygame.quit()


            exit()



        
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if steven_rect.collidepoint(event.pos) and steven_rect.bottom >= 300:

                

                
                print('collision')
                    
                steven_gravity = -25

        
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and steven_rect.bottom >= 390:
                steven_gravity = -25
                counter += 1

                
                 
           
        if game_active: 
           
            
            
        
            Steven1 = Steven()
            Steven1.steven_move()
            Pink1 = Pink()
            Pink1.pinkInput()
          
            
            Steven1.steven_move()

            
            
        

            
                    
        
        else:

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                
                game_active = True
                start_time = 0
                start_time = int(pygame.time.get_ticks() / 1000)
        if event.type == green_timer and game_active :
            green_rect_list.append(green_image.get_rect(midleft = (randint(500,600), 300)))
        
        if event.type == green_timer and game_active :
            screen.blit(Garnet_image, Garnet_rect)     




            
   
            
        

    if game_active:
        
        
        
        screen.blit(sky_image, (0,0))
        screen.blit(ground_image, (0,325))
        color = (255, 200, 200)
        biscoito.updateCookie()
        biscoito.display_score()
        screen.blit(steven_image, steven_rect)
        
        steven = Steven()
        Pink1 = Pink()
        Pink1.movePink()
        on = 20
        
        
        screen.blit(Peri_image, Peri_rect)
        
        
        
        screen.blit(green_image, green_rect)
        Green1 = Green()
        Green1.moveGreen()
        green_rect_list = green_movement(green_rect_list)
        
      
        
        Green1.collisionsGreen()

        
    
        
        

        if steven_rect.colliderect(Peri_rect): 
            
               

                video = VideoFileClip('test.mp4')
                video.preview()
                exit()
                p = multiprocessing.Process(playsound('Abertura.mp3'), False)
                p.terminate()
        
                
        
        
        
        steven_gravity += 1 
        steven_rect.y +=  steven_gravity

        if steven_rect.bottom >= 390:

                    
            steven_rect.bottom = 390
        
        if steven_rect.right <= - 100 or steven_rect.left >= 800:
                  
            steven_rect.right = 80
        
        if steven_rect.colliderect(green_rect) and steven_rect.colliderect(Peri_rect):
            counter = counter - counter
 
    else:

        screen.fill((200,200,200)) 
        ste_surface = pygame.image.load('capa.jpeg').convert_alpha()
        default_ste_size = (800, 400)
        ste_image = pygame.transform.scale(ste_surface, default_ste_size)
        ste_rect = ste_image.get_rect(center = (400, 200))
        screen.blit(ste_image, ste_rect)
        stev_surface = pygame.image.load('steven.png').convert_alpha()
        default_stev_size = (100, 100)
        stev_image = pygame.transform.scale(stev_surface, default_stev_size)
        stev_rect = stev_image.get_rect(midleft = (600, 400))
        screen.blit(stev_image, stev_rect)
        start_time = pygame.time.get_ticks()
        current_time = int(pygame.time.get_ticks() / 1000 ) - start_time
        counter = counter - counter
	

		
        

        
    pygame.display.update()
    clock.tick(60)
