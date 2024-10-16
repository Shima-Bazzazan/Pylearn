
import random 
import arcade


class Snake(arcade.Sprite):
    def __init__(self , game):
        super().__init__()
        self.width = 33
        self.height = 33
        self.center_x = game.width //  2
        self.center_y = game.height // 2
        self.color1 = arcade.color.LIGHT_BROWN
        self.color2 = arcade.color.DARK_BROWN
        self.change_x = 0 
        self.change_y = 0 
        self.speed = 3
        self.score= 0
        self.body = []
        self.radius = 12

    def move(self):
        self.body.append({"x" : self.center_x , "y" : self.center_y})
        if len(self.body) > self.score :
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
    
    def move_ai(self, center_x, center_y):
        self.body.append({"x" : self.center_x , "y" : self.center_y})
        if len(self.body) > self.score :
            self.body.pop(0)

        if self.center_y > center_y:
            self.center_y -= self.speed

        if self.center_y < center_y:
            self.center_y += self.speed

        if self.center_x < center_x:
            self.center_x += self.speed
            
        if self.center_x > center_x:
            self.center_x -= self.speed
    
    def mydraw(self) :
        arcade.draw_circle_filled(self.center_x  , self.center_y , self.radius , self.color1)
        i = 0 
        for part in self.body :
            if i % 2 == 0 :
                arcade.draw_circle_filled(part["x"] , part["y"] , self.radius  , self.color1)
            else :
                arcade.draw_circle_filled(part["x"] , part["y"] , self.radius  , self.color2)
            i += 1

    def eat_apple(self , apple):
        del apple
        self.score += 1

    def eat_pear(self , pear):
        del pear
        self.score += 2

    def eat_poo(self , poo):
        del poo
        self.score -= 1