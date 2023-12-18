
import arcade

class Heart(arcade.Sprite):
    def __init__(self, location):
        super().__init__(".\\spaceship.png")
        self.center_x= 20 + location * 35
        self.center_y= 20
        self.width= 30
        self.height= 30
        self.angle= 335
