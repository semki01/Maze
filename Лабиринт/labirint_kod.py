from turtle import window_height, window_width
from pygame import *

#mixer.init()
#mixer.music.load('jungles.ogg')
#mixer.music.play()

window_width = 700
window_height = 500
window = display.set_mode((window_width, window_height))
display.set_caption("Maze")
background = transform.scale(image.load('background.jpg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < window_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < window_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= window_width - 85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color = (color_1, color_2, color_3)
        self.width = wall_width
        self.height = wall_height

        # картинка стены прямоугольник нужных размеров и цвета
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)

        #каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


player = Player('hero.png', 50, 410, 6)
enemy = Enemy('cyborg.png', 550, 280, 4)
finish = GameSprite('treasure.png', 580, 420, 10)

w1 = Wall(154, 205, 50, 100, 20, 480, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)
w4 = Wall(154, 205, 50, 190, 110, 10, 380)
w5 = Wall(154, 205, 50, 280, 20, 10, 380)
w6 = Wall(154, 205, 50, 370, 110, 10, 380)
w7 = Wall(154, 205, 50, 460, 20, 10, 380)
w8 = Wall(154, 205, 50, 460, 400, 100, 10)


walls = [w1, w2, w3, w4, w5, w6, w7]



game = True
clock = time.Clock()
FPS  = 60
end = False

font.init()
font1 = font.SysFont('Arial',70)
win = font1.render('YOU WIN!', True, (255, 215, 0))
lose = font1.render('LOL', True, (180, 0, 0))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not end:
        window.blit(background, (0, 0))
        player.update()
        player.reset()
        enemy.update()
        enemy.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        finish.reset()

        for  wall in walls:
            if sprite.collide_rect(player, wall):
                end = True
                window.blit(lose, (200, 200))

    display.update()
    clock.tick(FPS)
