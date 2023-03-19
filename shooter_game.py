from pygame import *
from random import randint

font.init()

mixer.init()
mixer.music.load('space.ogg')
mixer.music.set_volume(0.2)
mixer.music.play(loops=-1)
fire_sound = mixer.Sound('music6.ogg')
WIDTH, HEIGHT = 700, 500
FPS = 60
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Шутер")
clock = time.Clock()

ufo_image = image.load("ufo2.png")
player_image = image.load("rocket3.png")
fire_image = image.load("bullet2.png")
asteroid_image = image.load("asteroid2.png")
capsule_image = image.load("capsule.png")


class GameSprite(sprite. Sprite):
    def __init__(self, sprite_img, width, height, x, y, speed = 15):
        super().__init__()
        self.image = transform.scale(sprite_img,(width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw(self):
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def __init__(self, sprite_img, width, height, x, y, speed = 15):
        super().__init__(sprite_img, width, height, x, y, speed = 15)
        self.hp = 3


    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < WIDTH - 80:
            self.rect.x += self.speed
    
    def fire(self):
        global superpower2
        if superpower:
            bullet4 = Bullet(fire_image , 10, 20, self.rect.centerx - 40, self.rect.y + 40)
            bullet7 = Bullet(fire_image , 10, 20, self.rect.centerx + 40, self.rect.y + 40)
            bullet5 = Bullet(fire_image , 10, 20, self.rect.centerx + 10, self.rect.y + 10)
            bullet6 = Bullet(fire_image , 10, 20, self.rect.centerx - 10, self.rect.y + 10)
            bullets.add(bullet4, bullet5, bullet6, bullet7)
        bullet = Bullet(fire_image , 10, 20, self.rect.centerx, self.rect.y)
        bullet2 = Bullet(fire_image , 10, 20, self.rect.centerx + 20, self.rect.y + 5)
        bullet3 = Bullet(fire_image , 10, 20, self.rect.centerx - 20, self.rect.y + 5)
        bullets.add(bullet, bullet2, bullet3)
        fire_sound.play()
        if superpower2:
            bullet7 = Bullet(fire_image , 650, 20, self.rect.centerx - 325, self.rect.y)
            bullets.add(bullet7)
            superpower2 = False
            fire_sound.play()
        else:
            bullet = Bullet(fire_image , 10, 20, self.rect.centerx, self.rect.y)
            bullet2 = Bullet(fire_image , 10, 20, self.rect.centerx + 20, self.rect.y + 5)
            bullet3 = Bullet(fire_image , 10, 20, self.rect.centerx - 20, self.rect.y + 5)
            bullets.add(bullet, bullet2, bullet3)
            fire_sound.play()
        

class Enemy(GameSprite):
    def update(self):
        global lost
        ''' рух спрайту '''
        if self.rect.y < HEIGHT:
            self.rect.y += self.speed
        else:
            lost +=1
            lost_text.set_text("Пропущено:" + str(lost))
            self.rect.y = randint(-500, -100)
            self.rect.x = randint(0, WIDTH - 70)
            self.speed = randint(2, 5)


class Text(sprite.Sprite):
    def __init__(self, text, x, y, font_size=22, font_name="Impact", color = (255, 255, 255)):
        self.font = font.SysFont(font_name, font_size)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
    def draw(self):
        window.blit(self.image, self.rect)

    def set_text(self, new_text):
        self.image = self.font.render(new_text, True, self.color)

class Bullet(GameSprite):
    def update(self):
        ''' рух спрайту '''
        if self.rect.y > -100:
            self.rect.y -= self.speed
        else:
            self.kill()

class Asteroid(GameSprite):
    def update(self):
        global lost
        ''' рух спрайту '''
        if self.rect.y < HEIGHT:
            self.rect.y += self.speed
        else:
            self.rect.y = randint(-500, -100)
            self.rect.x = randint(0, WIDTH - 70)
            self.speed = randint(4, 6)

class Capsule(GameSprite):
    def update(self):
        global lost
        ''' рух спрайту '''
        if self.rect.y < HEIGHT:
            self.rect.y += self.speed
        else:
            self.kill()

lost_text = Text("Пропущено: 0", 20, 20)
score_text = Text("Збито: 0", 20, 50)
hp_text = Text("Життя: 3", 20 , 80)
bg = transform.scale(image.load("stairrssky.jpg"), (WIDTH, HEIGHT))
bg2 = transform.scale(image.load("stairrssky.jpg"), (WIDTH, HEIGHT))
bg1_y = 0
bg2_y = -HEIGHT
player = Player(player_image, width = 100, height = 100, x = 350, y = 400)


asteroids = sprite.Group()
bullets = sprite.Group()
ufos = sprite.Group()
capsule = sprite.Group()
for i in range(3):
    rand_y = randint(-500, -100)
    rand_x = randint(0, WIDTH - 70)
    rand_speed = randint(2, 4)
    ufos.add(Enemy(ufo_image, width = 80, height = 50, x = rand_x, y = rand_y, speed = rand_speed))

for i in range(1):
    rand_y = randint(-500, -100)
    rand_x = randint(0, WIDTH - 70)
    rand_speed = randint(4, 6)
    asteroids.add(Asteroid(asteroid_image, width = 30, height = 30, x = rand_x, y = rand_y, speed = rand_speed))

run = True
finish = False
superpower = False
superpower2 = False
clock = time.Clock()
FPS = 60
step = 3
score = 0
lost = 0

result_text = Text("Перемога!", WIDTH / 2 - 100, HEIGHT /2, font_size = 50)

font1 = font.SysFont("Impact", 50)
win = font1.render("YOU WIN!!!", True, (3, 66, 20))
lose = font1.render("YOU LOSE!!!", True, (255, 0, 0))

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
    if not finish:
        rand_num = randint(0, 600)
        if rand_num == 175:
            capsule.add(Capsule(capsule_image, width = 20, height = 40 , x = randint(0, 600),y = -150, speed = 2))
        asteroids.update()
        player.update()
        ufos.update()
        bullets.update()
        capsule.update()
        spritelist = sprite.groupcollide(ufos, bullets, True, True)
        for collide in spritelist:
            score += 1
            score_text.set_text("Рахунок:" + str(score))
            if score >= 5:
                superpower = True
            rand_y = randint(-500, -100)
            rand_x = randint(0, WIDTH - 70)
            rand_speed = randint(2, 5)
            ufos.add(Enemy(ufo_image, width = 80, height = 50, x = rand_x, y = rand_y, speed = rand_speed))
        spritelist = sprite.spritecollide(player, ufos, True)
        for collide in spritelist:
            player.hp -=1
            hp_text.set_text("Життя:"+str(player.hp))
            if player.hp == 0:
                finish = True
                result_text.set_text("YOU LOSE!")
        spritelist = sprite.spritecollide(player, capsule, True)
        for collide in spritelist:
            superpower2 = True
        spritelist = sprite.spritecollide(player, asteroids, False)
        for collide in spritelist:
            finish = True
            result_text.set_text("YOU LOSE!")
        if lost >= 10:
            finish  = True
            result_text.set_text("YOU LOSE")
        if score >= 20:
            finish = True
        window.blit(bg, (0, bg1_y))
        window.blit(bg2, (0, bg2_y))
        bg1_y +=1
        bg2_y +=1
        if bg1_y > HEIGHT:  
            bg1_y = -HEIGHT
        if bg2_y > HEIGHT:
            bg2_y = -HEIGHT
        player.draw()
        ufos.draw(window)
        bullets.draw(window)
        asteroids.draw(window)
        capsule.draw(window)
    else:
        result_text.draw()
    lost_text.draw()
    score_text.draw()
    hp_text.draw()
    display.update()
    clock.tick(FPS)