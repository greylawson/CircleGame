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
    SpriteManager.spawn(JiggleBot (200, 50, 20))
    SpriteManager.spawn(Enemy(100, 100, 2))
    
    enemyTeam = 2
    
    sprites.append(player)
    sprites.append(Enemy(50, 50, enemyTeam))
    sprites.append(Enemy(150, 150, enemyTeam))
    sprites.append(raindrop(50, 200, enemyTeam))
    sprites.append(raindrop(100, 200, enemyTeam))
    sprites.append(raindrop(150, 200, enemyTeam))
    sprites.append(raindrop(200, 200, enemyTeam))
    sprites.append(raindrop(250, 200, enemyTeam))
    sprites.append(raindrop(300, 200, enemyTeam))
    sprites.append(raindrop(350, 200, enemyTeam))
    sprites.append(raindrop(400, 200, enemyTeam))
    sprites.append(raindrop(450, 200, enemyTeam))
    sprites.append(raindrop(500, 200, enemyTeam))
    sprites.append(ScreenSaverBot(20, 150, enemyTeam))
    sprites.append(JiggleBot(20, 100, enemyTeam))
                           
def draw():
    global player, sprites
    background(255)    

    for sprite in sprites:
        sprite.animate()
    
def keyPressed():
    SpriteManager.player.keyDown()    
        
def keyReleased():
    SpriteManager.player.keyUp()
