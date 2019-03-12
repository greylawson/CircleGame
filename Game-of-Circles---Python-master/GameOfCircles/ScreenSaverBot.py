from Sprite import Sprite

class ScreenSaverBot(Sprite):
    
    xspeed = 8
    yspeed = 4
    diameter = 50
    c = color(255,255,0)
    
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.x < 25 or self.x > width-25:
            self.xspeed *= -1
        if self.y < 25 or self.y > height-25:
            self.yspeed *= -1
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
