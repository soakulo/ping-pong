from pygame import *
font.init()

window = display.set_mode((700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, width, height, player_x, player_y, player_speed):
        super().__init__()
        self.player_speed = player_speed
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def colliderect(self, sprite):
        return self.rect.colliderect(sprite.rect)

class Platform(GameSprite):
    def update(self):
        global speed
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >=0:
            self.rect.y -= speed
        if keys_pressed[K_s] and self.rect.y <= 400:
            self.rect.y += speed
class Platform2(GameSprite):
    def update(self):
        global speed
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >=0:
            self.rect.y -= speed
        if keys_pressed[K_DOWN] and self.rect.y <= 400:
            self.rect.y += speed
class Ball(GameSprite):
    def update(self):
        global ball_speed_x
        global ball_speed_y
        self.rect.x -= ball_speed_x
        self.rect.y -= ball_speed_y
        if self.colliderect(platform) or self.colliderect(platform2):
            ball_speed_x *= -1
            ball_speed_y *-1
        if self.rect.x == 0 or self.rect.x > 650:
            ball_speed_x *= -1
        if self.rect.y == 0 or self.rect.y > 450:
            ball_speed_y *= -1

clock = time.Clock()
ball = Ball("ball.png", 50, 50, 240, 300, 10)
platform = Platform("platform.png", 30, 100, 100, 200, 10)
platform2 = Platform2("platform.png", 30, 100, 550, 200, 10)

lose = font.SysFont('Arial', 40).render("YOU LOST", True, (200, 0, 0))
win = font.SysFont('Arial', 40).render("YOU WON", True, (0, 200, 0))

speed = 5

ball_speed_x = 5
ball_speed_y = 5

platform_x = 0

game = True
Finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            exit()
    while Finish != True:
        window.fill((200, 255, 255))
        for e in event.get():
            if e.type == QUIT:
                exit()
        if ball.rect.x == 30 or ball.rect.x == 650:
            window.blit(lose, (300, 250))
            Finish = True
        if ball.rect.y == 450:
            window.blit(lose, (300, 250))
            Finish = True
        platform.update()
        platform.reset()
        platform2.update()
        platform2.reset()
        ball.update()
        ball.reset()
        display.update()
        clock.tick(60)
display.update()