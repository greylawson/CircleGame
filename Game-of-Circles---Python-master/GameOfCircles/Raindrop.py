import SpriteManager
from Sprite import Sprite

class Raindrop(Sprite):
    
    speed = 8
    diameter = 50
    c = color(0,0,255)
    
    def __init__(self, x, y, team):
        self.x = random(0, width)
        self.y = random(0, height)
        self.team = team
        
    def move(self):
        self.y += self.speed
        if self.y < 0:
            self.speed *= -1
        if self.y > width:
            self.y = 0 
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
