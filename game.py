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

    def setup(self):
        self.background = arcade.load_texture('images/background.png')
        self.tiles_sprite_list = arcade.SpriteList()
        self.game_field = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
        tile_list_x = {
            1: 71, 2: 208, 3: 345, 4: 482,
            5: 71, 6: 208, 7: 345, 8: 482,
            9: 71, 10: 208, 11: 345, 12: 482,
            13: 71, 14: 208, 15: 345, 16: 482
        }
        tile_list_y = {
            1: 482, 2: 482, 3: 482, 4: 482,
            5: 345, 6: 345, 7: 345, 8: 345,
            9: 208, 10: 208, 11: 208, 12: 208,
            13: 71, 14: 71, 15: 71, 16: 71
        }
        self.game_field[3][0] = Tile('2', tile_list_x[13], tile_list_y[13])  # 13

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.draw_tiles()

    def draw_tiles(self):
        for row in self.game_field:
            for tile in row:
                if tile:
                    tile.draw()

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        pass

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
