import SpriteManager
from Sprite import Sprite
from Bullet import Bullet

class Shooter(Sprite):
    
    speed = 8
    diameter = 50
    c = color(0,0,255)
    
    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector )
        
    def aim(self, target):
        return PVector(0, 10)
    
    def fire(self, vector):
        SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
