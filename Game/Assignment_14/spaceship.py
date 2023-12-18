
import arcade
from bullet import Bullet

class Spaceship(arcade.Sprite):
    def __init__(self, game):
        super().__init__(".\\spaceship.png")
        self.center_x= game.width // 2
        self.center_y= 45
        self.change_x= 0
        self.change_y= 0
        self.width=  90
        self.height= 80
        self.speed= 4
        self.game_width= game.width
        self.bullet_list= []
        
    def move (self):
        if self.change_x== 1:
            if self.center_x < (self.game_width - self.width // 2):
                self.center_x += self.speed
        
        elif self.change_x== -1:
            if self.center_x > self.width // 2:
                self.center_x -= self.speed

    
    def fire (self):
        new_bullet= Bullet(self)
        self.bullet_list.append (new_bullet)
