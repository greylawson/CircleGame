import platform
import platform
from Bullet import Bullet 
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from raindrop import raindrop
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot
import SpriteManager

def setup():
    print "Built with Processing Python version " + platform.python_version()
    size(800, 800)
    
    
    player = Player(width / 2, height - 100, 1);
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(player)
    
    enemyTeam = 2
    
    SpriteManager.spawn(Enemy(0, 50, 2))
    SpriteManager.spawn(Enemy(50, 100, 2))
    SpriteManager.spawn(Enemy(100, 150, 2))
    SpriteManager.spawn(Enemy(150, 200, 2))
    
    SpriteManager.spawn(raindrop(50, 200, 2))
    SpriteManager.spawn(raindrop(100, 200, 2))
    SpriteManager.spawn(raindrop(150, 200, 2))
    SpriteManager.spawn(raindrop(200, 200, 2))
    SpriteManager.spawn(raindrop(250, 200, 2))
    SpriteManager.spawn(raindrop(300, 200, 2))
    SpriteManager.spawn(raindrop(350, 200, 2))
    SpriteManager.spawn(raindrop(400, 200, 2))
    SpriteManager.spawn(raindrop(450, 200, 2))
    SpriteManager.spawn(raindrop(500, 200, 2))
    
    SpriteManager.spawn(ScreenSaverBot(20, 150, enemyTeam))
    
    SpriteManager.spawn(JiggleBot(50, 100, enemyTeam))
    SpriteManager.spawn(JiggleBot(200, 100, enemyTeam))
                           
def draw():
    background(0)
    SpriteManager.animate()


def keyPressed():
    SpriteManager.player.keyDown()    
        
def keyReleased():
    SpriteManager.player.keyUp()
