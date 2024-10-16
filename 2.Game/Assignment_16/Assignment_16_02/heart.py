import arcade

class Heart(arcade.Sprite):
    def __init__(self, x):
        super().__init__(".\\paddle.png")
        self.center_x = x * 33
        self.center_y = 13
        self.width = 30
        self.height = 8