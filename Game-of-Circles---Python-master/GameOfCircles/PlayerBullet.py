from Sprite import Sprite

import SpriteManager

class PlayerBullet(Sprite):
    speed = 1.5
    diameter = 10
    c = color(255,225,0)
    
    def __init__(self, x, y, vector, team):
        Sprite.__init__(self, x, y, team)
        self.vector = vector


    def move(self):
        self.x += self.vector.x * self.speed
        self.y += self.vector.y * self.speed
        if(self.x < 0 - self.diameter
        or self.x > width + self.diameter
        or self.y > height + self.diameter
        or self.y < 0 - self.diameter):
            SpriteManager.destroy(self)
