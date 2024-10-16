
import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self, game):
        super().__init__(".\\enemy.png")
        self.center_x= random.randint(0, game.width) 
        self.center_y= game.height + 50
        self.width=  90
        self.height= 90
        self.angle=180
        self.speed= 2
    
    def move(self):
        self.center_y-= self.speed

    def rise_speed(self):
        self.speed += 2
