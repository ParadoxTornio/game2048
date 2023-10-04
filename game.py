import arcade
from sprites import Tile
from config import *


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = None
        self.tiles_sprite_list = None

    def setup(self):
        self.background = arcade.load_texture('images/background.png')
        self.tiles_sprite_list = arcade.SpriteList()
        self.tiles_sprite_list.append(Tile('512', 71, 482))  # 1
        self.tiles_sprite_list.append(Tile('256', 208, 482))  # 2
        self.tiles_sprite_list.append(Tile('128', 345, 482))  # 3
        self.tiles_sprite_list.append(Tile('64', 482, 482))  # 4
        self.tiles_sprite_list.append(Tile('512', 71, 345))  # 5
        self.tiles_sprite_list.append(Tile('1024', 208, 345))  # 6
        self.tiles_sprite_list.append(Tile('2048', 345, 345))  # 7
        self.tiles_sprite_list.append(Tile('1024', 482, 345))  # 8
        self.tiles_sprite_list.append(Tile('32', 71, 208))  # 9
        self.tiles_sprite_list.append(Tile('64', 208, 208))  # 10
        self.tiles_sprite_list.append(Tile('128', 345, 208))  # 11
        self.tiles_sprite_list.append(Tile('256', 482, 208))  # 12
        self.tiles_sprite_list.append(Tile('2', 71, 71))  # 13
        self.tiles_sprite_list.append(Tile('4', 208, 71))  # 14
        self.tiles_sprite_list.append(Tile('8', 345, 71))  # 15
        self.tiles_sprite_list.append(Tile('16', 482, 71))  # 16

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background),
        self.tiles_sprite_list.draw()

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
