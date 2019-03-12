from Sprite import Sprite

class JiggleBot(Sprite):
    
    speed = 4
    diameter = 50
    c = color(0, 255, 0)
        
    def move(self):
        self.y += random(-self.speed, self.speed)
        self.x += random(-self.speed, self.speed)
        self.x = constrain(self.x, 0, width)
        self.x = constrain(self.y, 0, height)
