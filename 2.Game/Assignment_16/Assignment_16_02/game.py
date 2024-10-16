
import arcade
from board import Board
from ball import Ball
from brick import Brick
from heart import Heart

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width= 500, height= 400, title= "BreakOut")
        self.color = arcade.color.LIGHT_SKY_BLUE
        arcade.set_background_color (self.color)
        self.board = Board(self)
        self.ball = Ball(self)
        self.life = 3
        self.hearts = []
        self.bricks = []
        self.flag = 1

        for i in range(5):
            row = []
            for j in range(10):
                if j%2 == 0:
                    color = arcade.color.LIGHT_PASTEL_PURPLE
                else:
                    color = arcade.color.LIGHT_PINK
                brick = Brick(self, j, i + 1, color)
                row.append(brick)
            self.bricks.append(row)


        for i in range(self.life):
            heart = Heart(i + 1)
            self.hearts.append(heart)


    def on_draw(self):
        arcade.start_render()

        self.board.draw()
        self.ball.draw()
        for i in self.hearts:
            i.draw()
        for i in self.bricks:
            for j in i:
                j.draw()
        arcade.draw_text(f"Score: {self.board.score}", self.width - 90, 10, arcade.color.RED, 13, 1, font_name= "arial", bold=True)

        if self.flag == 0:
            self.clear()
            arcade.draw_text("Game Over", self.width//2 -105, self.height//2, arcade.color.RED, 24, 1, bold=True)

        arcade.finish_render()

    def on_key_press(self, symbol, modifiers):
        if symbol==arcade.key.RIGHT:
            self.board.change_x=1

        if symbol==arcade.key.LEFT:
            self.board.change_x=-1

    def on_mouse_motion(self, x, y, dx, dy):
        if 30 < x < self.width-30:
            self.board.center_x=x

    def on_update(self, delta_time):
        self.ball.move()
        self.board.move()

        if self.ball.center_x < self.ball.width//2:
            self.ball.change_x = 1
        elif self.ball.center_x > self.width - self.ball.width//2:
            self.ball.change_x = -1

        if self.ball.center_y > self.height - self.ball.height//2:
            self.ball.change_y = -1
    
        if arcade.check_for_collision(self.ball, self.board):
            self.ball.change_y = 1

        if self.ball.center_y < 0:
            del self.ball
            self.ball = Ball(self.board)
            self.board.score-=1
            if self.life>0:
                self.life -= 1
                self.hearts.remove(self.hearts[self.life])
        
        if self.board.center_x < 30 or self.board.center_x > self.width - 30:
            self.board.change_x = 0

        for row in self.bricks:
            for brick in row:
                if arcade.check_for_collision(self.ball, brick):
                    self.ball.change_y *= -1
                    row.remove(brick)
                    self.board.score +=1

        for raw in self.bricks:
            if len(raw) == 0:
                self.bricks.remove(raw)
                for row2 in self.bricks:
                    for brick in row2:
                        brick.center_y -= 20
                new_row = []
                for j in range(10):
                    if j%2 == 0:
                        color = arcade.color.LIGHT_PASTEL_PURPLE
                    else:
                        color = arcade.color.LIGHT_PINK
                    brick = Brick(self, j, 5, color)
                    new_row.append(brick)
                self.bricks.append(new_row)
        if self.life == 0:
            self.flag = 0