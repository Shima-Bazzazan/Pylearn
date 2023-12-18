
import random
import arcade

class Food(arcade.Sprite):
    def __init__(self, game, food_type):
        super().__init__(food_type)
        self.width=35
        self.height=35
        self.center_x=random.randint(self.width //2 , game.width - self.width //2)
        self.center_y=random.randint(self.height //2 , game.height - self.height //2)
        self.change_x=0
        self.change_y=0