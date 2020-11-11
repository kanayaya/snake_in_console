import os
import keyboard

import menus
import snake


class MainManager:
    def __init__(self):
        self.menu_object = menus.Menu(menus.all_menus_dict)
        self.menu_object.show_menu()
        self.key_of_choise = 0
        keyboard.on_press(lambda key: self.choose_manager(key))
        keyboard.wait('esc')
        os.system('cls')

    def choose_manager(self, key):
        if self.key_of_choise == 0:
            self.menu_object.manage_menu(key)
        elif self.key_of_choise == 1:
            snake.start_game()
            self.key_of_choise = 2
            self.choose_manager('shift')
        elif self.key_of_choise == 2:
            snake.Snake


if __name__ == '__main__':
    MM = MainManager()




