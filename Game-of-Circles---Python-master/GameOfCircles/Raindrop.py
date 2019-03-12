from Sprite import Sprite

class raindrop(Sprite):
    
    speed = 8
    diameter = 20
    c = color(255,0,255)
    
    def __init__(self, x, y, team):
        self.x = random(0,780)
        self.y = random(0,50)
        self.team = team
        
    def move(self):
        self.y += self.speed
        if self.y < 0:
            self.speed *= -1
        if self.y > width:
            self.y = 0
