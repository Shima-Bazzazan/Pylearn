
import arcade
from snake import Snake
from apple import Apple
from pear import Pear 
from poo import Poo


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width= 500 , height=500 , title="Super Snake 🐍 V1")
        arcade.set_background_color(arcade.color.KHAKI)
        self.apple = Apple(self) 
        self.pear  = Pear(self)        
        self.snake = Snake(self)
        self.poo = Poo(self)
        self.flag= 1

    def on_draw(self):
        
        if self.flag == 1:
            arcade.start_render()
            self.apple.draw()
            self.pear.draw()
            self.poo.draw()
            self.snake.mydraw()
            arcade.draw_text("Score: "+ str(self.snake.score), self.width-103, 15, arcade.color.BLACK, 15, 12)
        
        elif self.flag == 0:
            arcade.draw_text("Game Over", 130, self.height//2 , arcade.color.RED , 30 ,  bold=True) 
        arcade.finish_render()


    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP or symbol == arcade.key.W :
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D :
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif symbol == arcade.key.LEFT or symbol == arcade.key.A :
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif symbol == arcade.key.DOWN or symbol == arcade.key.S :
            self.snake.change_x = 0
            self.snake.change_y = -1 

    
    def on_update(self, delta_time : float) :
        self.snake.move()
        if arcade.check_for_collision(self.snake , self.apple ):
            self.snake.eat_apple(self.apple)
            self.apple = Apple(self)

        if arcade.check_for_collision(self.snake , self.pear ):
            self.snake.eat_pear(self.pear)
            self.pear = Pear(self)

        if arcade.check_for_collision(self.snake , self.poo ):
            if self.snake.score== 0:
                self.flag= 0
            self.snake.eat_poo(self.poo)
            self.poo = Poo(self)  
        
        if self.snake.center_x < 0 or self.snake.center_y < 0 or self.snake.center_x >self.width  or self.snake.center_y > self.height:
            self.flag = 0   
        
        for part in self.snake.body:
            if self.snake.center_x == part["x"] and self.snake.center_y == part["y"]:
                self.flag=0

if __name__ == "__main__":
    game = Game()
    arcade.run()