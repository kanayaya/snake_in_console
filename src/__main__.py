from time import sleep
import os
import keyboard

from . import menus
from . import snake


class MainManager:
    def __init__(self):
        """Сразу и конструктор и функция, запускающая игру"""
        self.menu_object = menus.Menu(menus.all_menus_dict)
        self.new_snake = snake.Snake()
        self.menu_object.show_menu(' ')
        self.key_of_choise = 0
        keyboard.on_press(lambda key: self.choose_manager(key))
        while True:    # Этот цикл позволяет начать игру и после проигрыша начать заново
            while True:    # Этот цикл проверяет, хочет ли пользователь начать игру или выйти
                sleep(0.3)
                if self.menu_object.exitvar:
                    keyboard.press_and_release('alt + f4')
                if self.menu_object.launch_game_var:
                    break
            self.key_of_choise = 2    # Меняем управление меню на управление змейкой
            os.system('cls')   # отсюда
            print(10*'\n')    # Экран, просящий нажать шифт, чтобы пользователь был готов
            print('Нажмите Shift')
            keyboard.wait('shift')    # досюда

            current_map, blacklist, map_lengh, map_width, food = snake.start_game(self.new_snake)
            while True:    # Этот цикл крутит игру
                food = snake.do_step(self.new_snake, current_map, blacklist, map_lengh, map_width, food)
                sleep(self.menu_object.difficulty)
                self.new_snake.move()
                if self.new_snake.bbreak:
                    break
            self.menu_object.launch_game_var = False
            self.key_of_choise = 0
            self.menu_object.current_menu = menus.change_menu(self.menu_object.menu_dict, 'lose_game')
            self.menu_object.show_menu(str(self.new_snake.counter))
            self.new_snake = snake.Snake()

    def choose_manager(self, key):
        """Так как считывает клавиши лишь одна функция, а управлять игрой надо двумя разными способами,
        функцию приходится делить"""
        if self.key_of_choise == 0:
            self.menu_object.manage_menu(key)

        elif self.key_of_choise == 2:
            self.new_snake.manage(key)


if __name__ == '__main__':
    MM = MainManager()




