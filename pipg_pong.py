from pygame import *
from random import *
font.init()
font = font.Font(None, 70)

mixer.init()
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('1602369695.9464e0wuv0xecopv2xki7ggeliteebr3xkvhtyha.jpg'), (700, 500))
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    skip = 0
    point = 0
    def __init__(self, paint, skale, speed, x, y, ypravlenie):
        super().__init__()
        self.image = transform.scale(image.load(paint), skale)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
        self.ypravlenie = ypravlenie

    def otobrazi(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        if self.ypravlenie == 'da':
            keys_pressed = key.get_pressed()
            if keys_pressed[K_d] and self.rect.x < 595:
                self.rect.x += self.speed
            if keys_pressed[K_a] and self.rect.x > 5:
                self.rect.x -= self.speed
        else:
            keys_pressed = key.get_pressed()
            if keys_pressed[K_RIGHT] and self.rect.x < 595:
                self.rect.x += self.speed
            if keys_pressed[K_LEFT] and self.rect.x > 5:
                self.rect.x -= self.speed

player1 = Player('images.jpg',(100, 100), 5, 300, 390,'da' )
player2 = Player('pngtree-ping-pong-paddle-isolated-on-transparent-background-png-image_16968660.webp',(100, 100), 5, 300, 50, 'Left,Up' )

game = True
while game:
    window.blit(background, (0, 0))

    player1.update()
    player1.otobrazi()
    player2.update()
    player2.otobrazi()

    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()
