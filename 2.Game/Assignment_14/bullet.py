
import arcade

class Bullet (arcade.Sprite):
    def __init__(self, spaceship):
        super().__init__(":resources:images/space_shooter/laserBlue01.png")
        self.center_x= spaceship.center_x
        self.center_y= spaceship.center_y + spaceship.height // 2
        self.change_x= 0
        self.change_y= 1
        self.angle= 90
        self.speed= 3
    
    def move(self):
        self.center_y += self.speed

    def rise_speed(self):
        self.speed += 1