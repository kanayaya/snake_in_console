import os, sys

import keyboard


class Menu():
    def __init__(self, menu_dict):
        self.menu_dict = menu_dict
        self.current_menu = change_menu(self.menu_dict, 'main_menu')

    def start(self):
        self.show_menu()
        keyboard.on_press(self.manage_menu)
        keyboard.wait('esc')

    def show_menu(self):
        """Показывает меню, выбранным считается пункт со вторым пунктом True"""
        os.system('cls')
        print(self.current_menu[0])
        print(10 * '\n')
        tab = 6 * '\t'
        for i in range(1, len(self.current_menu)):
            if self.current_menu[i][1]:
                print(tab + '>' + self.current_menu[i][0] + '<')
            else:
                print(tab + ' ' + self.current_menu[i][0])

    def manage_menu(self, key):
        """Позволяет управлять меню с помощью кнопок W и S на клавиатуре. когда выбор произведен,
        нажат Enter, меняет переменную menu_dict_key и переходит в другое меню"""
        menu_keys_dict = {
            'w' : -1,
            's' : 1,
            'up' : -1,
            'down' : 1,
        }
        if key.name in menu_keys_dict:
            self.current_menu = self.change_position(menu_keys_dict, key)
            self.show_menu()

        elif key.name == 'enter':
            for i in range(1, len(self.current_menu)):
                if self.current_menu[i][1]:
                    os.system('cls')
                    self.current_menu = self.current_menu[i][2](self.menu_dict, self.current_menu[i][3])
                    self.show_menu()
                    break

        else:
            pass

    def change_position(self, menu_keys_dict, key):
        """Меняет позицию выбора в менюшке, перетаскивая '> <' по пунктам"""
        position = 0
        for i in range(len(self.current_menu)):
            if self.current_menu[i][1]:
                position = i
        self.current_menu[position][1] = False

        if position + menu_keys_dict[key.name] == len(self.current_menu):
            position = 1
            self.current_menu[position][1] = True

        elif position + menu_keys_dict[key.name] < 1:
            position = len(self.current_menu) - 1
            self.current_menu[position][1] = True

        else:
            self.current_menu[position + menu_keys_dict[key.name]][1] = True

        return  self.current_menu

def change_menu(menu_dict, dict_key):
    return menu_dict[dict_key]

def exit_game(*no_args_but_they_will_come):
    keyboard.press_and_release('Ctrl + shift + c')


newgame_settings_list = []
lose_menu_list = []
options_menu_list = [
    'Настройки',
    ['Настройки', True, change_menu, 'options'],
    ['Настройки', False, change_menu, 'options'],
    ['Настройки', False, change_menu, 'options'],
]

main_menu_list = [
    'Главное меню',
    ['Новая игра', True, change_menu, 'new_game'],
    ['Рекорды', False, change_menu, 'scores'],
    ['Настройки', False, change_menu, 'options'],
    ['Выход', False, exit_game, 'no'],
]

all_menus_dict = {
    'main_menu' : main_menu_list,
    'options' : options_menu_list,
    'new_game' : newgame_settings_list,
}

menu_object = Menu(all_menus_dict)
menu_object.start()
