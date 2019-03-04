import platform
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from Raindrop import Raindrop
from Jiggle import Jiggle
from Shooter import Shooter
from ScreenSaver import ScreenSaver
from SpriteManager import sprites
from Sprite import Sprite
import SpriteManager

def setup():
    print "Built with Processing Python version " + platform.python_version()
    size(900, 900)
    player = Player(width/2, height/2, 1)
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(Jiggle(200, 50, 2))
    SpriteManager.spawn(Enemy(100, 100, 2))
    
    SpriteManager.spawn(Raindrop(200, 200, 2))
    SpriteManager.spawn(Raindrop(550, 100, 2))
    SpriteManager.spawn(Raindrop(500, 100, 2))
    SpriteManager.spawn(Raindrop(450, 100, 2))
    SpriteManager.spawn(Raindrop(400, 100, 2))
    SpriteManager.spawn(Raindrop(350, 100, 2))
    SpriteManager.spawn(Raindrop(300, 100, 2))
    SpriteManager.spawn(Raindrop(250, 100, 2))
    SpriteManager.spawn(Raindrop(200, 100, 2))
    SpriteManager.spawn(Raindrop(150, 100, 2))
    SpriteManager.spawn(Raindrop(100, 100, 2))
    
    SpriteManager.spawn(ScreenSaver(120, 100, 2))
     
    SpriteManager.spawn(Jiggle(100, 100, 2))
    
    SpriteManager.spawn(Shooter(100, 130, 2))
    
                           
def draw():
   background(255)
   SpriteManager.animate()
    
def keyPressed():
    global player
    SpriteManager.getPlayer().keyDown()
        
def keyReleased():
    global player
    SpriteManager.getPlayer().keyUp()
     
