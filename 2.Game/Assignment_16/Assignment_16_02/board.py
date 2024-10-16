import arcade

class Board(arcade.Sprite):
    def __init__(self, game):
        super().__init__(".\\paddle.png")
        self.center_x = game.width // 2
        self.center_y = 35
        self.change_x = 0
        self.change_y = 0
        self.width = game.width // 10 + 10
        self.height = 10
        self.color = arcade.color.SILVER_LAKE_BLUE
        self.speed = 4
        self.score = 0

    def move(self):
        self.center_x += self.change_x*self.speed