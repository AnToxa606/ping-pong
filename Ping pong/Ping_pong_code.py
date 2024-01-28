from pygame import *
img_back="img_back.png"
win_width = 800
win_height = 550
display.set_caption("Ping pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))



class GameSprite(sprite.Sprite):    
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


FPS=60
finish=False
run=True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    if not finish:
        window.blit(background, (0, 0))
        
        
    


        display.update()
    time.delay(FPS)