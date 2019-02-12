import platform
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from Raindrop import Raindrop
from Jiggle import Jiggle
from ScreenSaver import ScreenSaver
from SpriteManager import sprites

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(800, 800)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, playerTeam)
    
    sprites.append(player)
    sprites.append(Enemy(50, 50, enemyTeam))
    sprites.append(Enemy(150, 150, enemyTeam))
    
    sprites.append(Raindrop(550, 100, enemyTeam))
    sprites.append(Raindrop(500, 100, enemyTeam))
    sprites.append(Raindrop(450, 100, enemyTeam))
    sprites.append(Raindrop(400, 100, enemyTeam))
    sprites.append(Raindrop(350, 100, enemyTeam))
    sprites.append(Raindrop(300, 100, enemyTeam))
    sprites.append(Raindrop(250, 100, enemyTeam))
    sprites.append(Raindrop(200, 100, enemyTeam))
    sprites.append(Raindrop(150, 100, enemyTeam))
    sprites.append(Raindrop(100, 100, enemyTeam))
    
    sprites.append(ScreenSaver(120, 100, enemyTeam))
     
    sprites.append(Jiggle(100, 100, enemyTeam))
    
                           
def draw():
    global player, sprites
    background(255)    

    for sprite in sprites:
        sprite.animate()
        
    checkCollisions()
    
def checkCollisions():
    global sprites
    for a in sprites:
        for b in sprites:
            if a.team != b.team:
                d = (pow(a.x - b.x, 2) + pow(a.y - b.y, 2))**(0.5)
                r1 = a.diameter / 2
                r2 = b.diameter / 2
                if(r1 + r2 > d):
                    sprites.remove(a)
                    sprites.remove(b)
    
def keyPressed():
    global player
    player.keyDown()    
        
def keyReleased():
    global player
    player.keyUp()
