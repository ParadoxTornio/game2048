from typing import Union, List
import arcade
import random
from sprites import Tile
from config import *


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = None
        self.tiles_sprite_list = None
        self.game_field = None
        self.cord_dict_x = {0: 71, 1: 208, 2: 345, 3: 482}
        self.cord_dict_y = {0: 482, 1: 345, 2: 208, 3: 71}
        self.value_list = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
        self.level = 2

    def setup(self):
        self.background = arcade.load_texture('images/background.png')
        self.tiles_sprite_list = arcade.SpriteList()
        self.game_field: List[List[Union[int, Tile]]] = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
        self.random_tile()
        self.random_tile()

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.draw_tiles()

    def random_tile(self):
        while True:
            random_x = random.randint(0, 3)
            random_y = random.randint(0, 3)
            if self.game_field[random_y][random_x] == 0:
                self.game_field[random_y][random_x] = Tile(str(random.choice(self.value_list[0:self.level])),
                                                           self.cord_dict_y[random_y], self.cord_dict_x[random_x])
                break

    def draw_tiles(self):
        for row in self.game_field:
            for tile in row:
                if tile:
                    tile.draw()

    def move_up(self, y, x):
        pass

    def move_down(self, y, x):
        pass

    def move_right(self, y, x):
        pass

    def move_left(self, y, x):
        pass

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.UP:
            for y in range(1, 4):
                for x in range(4):
                    if self.game_field[y][x] != 0:
                        self.move_up(y, x)
                        print(y, x)

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


def main():
    """ Main function """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
