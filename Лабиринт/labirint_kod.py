from pygame import *

#mixer.init()
#mixer.music.load('jungles.ogg')
#mixer.music.play()

window = display.set_mode((700,500))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'), (700, 500))

x1 = 100
y1 = 300

x2 = 500
y2 = 300


class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
    #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
    #каждый спрайт должен иметь свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

sprite_1 = GameSprite('hero.png', 100, 100, 10)
sprite_2 = GameSprite('cyborg.png', 550, 260, 5)
gold = GameSprite('treasure.png', 550, 400, 0)

run = True

clock = time.Clock()
FPS = 60

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(background,(0, 0))
    sprite_1.reset()
    sprite_2.reset()
    gold.reset()
    display.update()
    clock.tick(60)

