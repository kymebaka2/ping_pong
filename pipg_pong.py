from pygame import *
from random import *

init()
mixer.init()
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('1602369695.9464e0wuv0xecopv2xki7ggeliteebr3xkvhtyha.jpg'), (700, 500))
clock = time.Clock()
FPS = 60
font.init()
font = font.Font(None, 70)

class GameSprite(sprite.Sprite):
    def __init__(self, paint, skale, speed_x, speed_y, x, y, ypravlenie, riko1 = False, riko2 = False,):
        super().__init__()
        self.image = transform.scale(image.load(paint), skale)
        self.rect = self.image.get_rect()
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect.x = x
        self.rect.y = y
        self.ypravlenie = ypravlenie
        self.riko1 = riko1
        self.riko2 = riko2

    def otobrazi(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        if self.ypravlenie == 'da':
            keys_pressed = key.get_pressed()
            if keys_pressed[K_d] and self.rect.x < 595:
                self.rect.x += self.speed_x
            if keys_pressed[K_a] and self.rect.x > 5:
                self.rect.x -= self.speed_x
        else:
            keys_pressed = key.get_pressed()
            if keys_pressed[K_RIGHT] and self.rect.x < 595:
                self.rect.x += self.speed_x
            if keys_pressed[K_LEFT] and self.rect.x > 5:
                self.rect.x -= self.speed_x

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.x >= 650 or self.rect.x <= 50:
            self.speed_x *= -1

player1 = Player('images.jpg',(100, 100), 5,5, 300, 390,'da', 'base' )
player2 = Player('images (2).jpg',(100, 100), 5,5, 300, 50, 'Left,Up', 'base' )
ball = Ball('images (1).jpg', (60,60), 5, 5, 250,250, 'go', 'down_right')
lose = font.render('LOSE', True, (255, 0, 0))

game = True
false = False
while game:
    window.blit(background, (0, 0))

    
    player1.otobrazi()
    
    player2.otobrazi()
    ball.otobrazi()
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    if false == False:
        ball.update()
        player2.update()
        player1.update()
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            ball.speed_y *= -1 
        if ball.rect.y <= 50 or ball.rect.y >= 550:
            false = True
    
    if false == True:
        window.blit(lose, (275,210))
    clock.tick(FPS)
    display.update()   
quit()
