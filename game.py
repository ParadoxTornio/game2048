import time
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
        self.score = 0
        self.level = 2
        self.quit_game_counter = 0
        self.my_file = open('score.txt', 'r+', encoding='utf-8')

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
        self.random_tile()
        self.random_tile()

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        arcade.draw_text(str(self.score), 90, SCREEN_HEIGHT - 33, arcade.color.BLACK, 16, 50, font_name='Arial')
        if self.score >= self.level * 500:
            self.level += 1
        for i in self.game_field:
            for j in i:
                if j:
                    self.quit_game_counter += 1
        if self.quit_game_counter == 16:
            time.sleep(1)
            self.my_file.write('score = ' + str(self.score) + '\n')
            self.my_file.write('game field = ' + str(self.game_field))
            self.my_file.close()
            exit()
        else:
            self.quit_game_counter = 0
        self.draw_tiles()

    def random_tile(self):
        while True:
            random_x = random.randint(0, 3)
            random_y = random.randint(0, 3)
            if self.game_field[random_y][random_x] == 0:
                add_value = random.choice(self.value_list[0:self.level])
                self.game_field[random_y][random_x] = Tile(add_value,
                                                           self.cord_dict_y[random_y], self.cord_dict_x[random_x])
                self.score += add_value
                break

    def draw_tiles(self):
        for row in self.game_field:
            for tile in row:
                if tile:
                    tile.draw()

    def move_up(self, y, x):
        while y > 0:
            new_y = y - 1
            if self.game_field[new_y][x] == 0:
                self.game_field[new_y][x] = self.game_field[y][x]
                self.game_field[new_y][x].center_y = self.cord_dict_y[new_y]
            elif self.game_field[new_y][x].value == self.game_field[y][x].value:
                self.game_field[new_y][x].change_value()
                new_y -= 1
            else:
                break
            self.game_field[y][x] = 0
            y = new_y

    def move_down(self, y, x):
        while y < 3:
            new_y = y + 1
            if self.game_field[new_y][x] == 0:
                self.game_field[new_y][x] = self.game_field[y][x]
                self.game_field[new_y][x].center_y = self.cord_dict_y[new_y]
            elif self.game_field[new_y][x].value == self.game_field[y][x].value:
                self.game_field[new_y][x].change_value()
                new_y += 1
            else:
                break
            self.game_field[y][x] = 0
            y = new_y

    def move_right(self, y, x):
        while x < 0:
            new_x = x + 1
            if self.game_field[y][new_x] == 0:
                self.game_field[y][new_x] = self.game_field[y][x]
                self.game_field[y][new_x].center_x = self.cord_dict_x[new_x]
            elif self.game_field[y][new_x].value == self.game_field[y][x].value:
                self.game_field[y][new_x].change_value()
                new_x += 1
            else:
                break
            self.game_field[y][x] = 0
            x = new_x

    def move_left(self, y, x):
        while x > 0:
            new_x = x - 1
            if self.game_field[y][new_x] == 0:
                self.game_field[y][new_x] = self.game_field[y][x]
                self.game_field[y][new_x].center_x = self.cord_dict_x[new_x]
            elif self.game_field[y][new_x].value == self.game_field[y][x].value:
                self.game_field[y][new_x].change_value()
                new_x -= 1
            else:
                break
            self.game_field[y][x] = 0
            x = new_x

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
            self.random_tile()

        if key == arcade.key.DOWN:
            for y in range(2, -1, -1):
                for x in range(4):
                    if self.game_field[y][x] != 0:
                        self.move_down(y, x)
            self.random_tile()

        if key == arcade.key.LEFT:
            for y in range(0, 4):
                for x in range(4):
                    if self.game_field[y][x] != 0:
                        self.move_left(y, x)
            self.random_tile()

        if key == arcade.key.RIGHT:
            for y in range(0, 4):
                for x in range(4):
                    if self.game_field[y][x] != 0:
                        self.move_right(y, x)
            self.random_tile()

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
