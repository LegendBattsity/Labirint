from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):

    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)

    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= 10
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += 10
        if keys_pressed[K_DOWN] and self.rect.y < 595:
            self.rect.y += 10


class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Sureface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Enemy(GameSprite):

    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)

    def update(self):
        if self.rect.x >= 640:
            self.side = 'left'
        if self.rect.x <= 510:
            self.side = 'right'
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'), (700, 500))
hero = transform.scale(image.load('hero.png'), (50, 50))
cyborg = transform.scale(image.load('cyborg.png'), (50, 50))
cyborg = transform.scale(image.load('treasure.png'), (50, 50))
FPS = 60
clock = time.Clock()
mixer.init()
x1 = 50
y1 = 350
x2 = 450
y2 = 35
x3 = 600
y3 = 400

game = True
p1 = Player('hero.png', 150, 200, 60)
p2 = Enemy('cyborg.png', 450, 300, 2)
# p3 = Wall()
while game:
    mixer.music.load('jungles.ogg')
    window.blit(background, (0, 0))
    p1.reset()
    p1.update()
    p2.reset()
    p2.update()

    clock.tick(FPS)

    for e in event.get():
        if e.type == QUIT:
            game = false

    display.update()

mixer.music.play()

