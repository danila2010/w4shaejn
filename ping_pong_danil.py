from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, width, hieght, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width, hieght))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y > 450:
            self.rect.y += self.speed
    def update_r(self):   
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y > 450:
            self.rect.y += self.speed
back = (35, 85, 123)
window = display.set_mode((600,500))
window.fill(back)

game = True
finish= False
clock= time.Clock()
FPS = 60

raket1 = Player('', 30, 200, 50, 150, 5)
raket2 = Player('', 520, 200, 50, 150, 5)
ball = GameSprite('', 200, 200, 50, 50, 5)

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        raket1.update_l()
        raket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(raket1,ball) or sprite.collide_rect(raket2,ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y * -= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > 550:
            finish = True
            window.blit(lose2, (200, 200))

        raket1.reset()
        raket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)


















     
















