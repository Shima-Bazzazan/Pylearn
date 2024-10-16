
import arcade 

class Rocket(arcade.Sprite) :
    def __init__(self , center_x, center_y, color, name):
        super().__init__()
        self.center_x= center_x
        self.center_y= center_y
        self.change_x=0
        self.change_y=0
        self.color= color
        self.width= 10
        self.height= 60
        self.speed= 3
        self.score= 0
        self.name = name

    def move(self ,game ,  ball):
        if ball.center_x > game.width// 2 :
            if self.center_y > ball.center_y :
                self.change_y = -1 
           
            if self.center_y < ball.center_y :
                self.change_y = 1

            self.center_y += self.change_y * self.speed 

            if self.center_y < 50 :
                self.center_y  = 50
            
            if self.center_y > game.height - 50 :
                self.center_y = game.height - 50 

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x , self.center_y , self.width , self.height , color= self.color )