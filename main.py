import pygame, sys

HEIGHT = 720
WIDTH = 1280

def load_spritesheet(filename, rows, cols):
    spritesheet = pygame.image.load(filename).convert_alpha()
    sprite_width = spritesheet.get_width() // cols
    sprite_height = spritesheet.get_height() // rows
    frames = []
    
    for row in range(rows):
        for col in range(cols):
            frame_rect = pygame.Rect(col * sprite_width, row * sprite_height, sprite_width, sprite_height)
            frame = spritesheet.subsurface(frame_rect)
            frames.append(frame)
    
    return frames

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, frames):
        super().__init__()
        self.frames = frames
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.animation_speed = 0.01  # You can adjust this value to change the animation speed
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed * 1000:  # Convert animation speed to milliseconds
            self.last_update = now
            self.index = (self.index + 1) % len(self.frames)
            self.image = self.frames[self.index]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

light_mage_frames = load_spritesheet("assets/sprites/mage/PNG/24x32/mage-light.png",4,3)

mage = Player(640, 360, light_mage_frames)
sprites = pygame.sprite.Group(mage)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    sprites.update()
    screen.fill('#AADD11')
    sprites.draw(screen)

    pygame.display.update()
    clock.tick(60)


