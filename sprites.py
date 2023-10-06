import arcade


class Tile(arcade.Sprite):
    def __init__(self, value, center_y, center_x):
        super().__init__(f'images/num{value}.png', center_x=center_x, center_y=center_y)
        self.direction = None
        self.value = value
