from time import sleep
import os
import keyboard

from . import menus
from . import snake


class MainManager:
    def __init__(self):
        self.menu_object = menus.Menu(menus.all_menus_dict)
        self.new_snake = snake.Snake()
        self.menu_object.show_menu()
        self.key_of_choise = 0
        keyboard.on_press(lambda key: self.choose_manager(key))
        while True:
            while True:
                keyboard.wait('shift')
                if self.menu_object.launch_game_var:
                    break

            self.key_of_choise = 2
            current_map, blacklist, map_lengh, map_width, food = snake.start_game(self.new_snake)
            while True:
                print(self.key_of_choise)
                food = snake.do_step(self.new_snake, current_map, blacklist, map_lengh, map_width, food)
                sleep(self.menu_object.difficulty)
                self.new_snake.move()
                if self.new_snake.bbreak:
                    break
            self.new_snake = snake.Snake()
            self.menu_object.launch_game_var = False
            self.key_of_choise = 0
            self.menu_object.current_menu = menus.change_menu(self.menu_object.menu_dict, 'lose_game')
            self.menu_object.show_menu()
        keyboard.wait('esc')
        os.system('cls')

    def choose_manager(self, key):

        if self.key_of_choise == 0:
            self.menu_object.manage_menu(key)

        elif self.key_of_choise == 2:
            self.new_snake.manage(key)


if __name__ == '__main__':
    MM = MainManager()




